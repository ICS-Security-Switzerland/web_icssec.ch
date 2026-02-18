/**
 * Cloudflare Pages Function — POST /api/register
 *
 * Receives membership form data, validates it, and forwards to Webling API.
 * Environment variables (set in Cloudflare Pages dashboard → Settings → Environment variables):
 *   WEBLING_API_KEY   – API key for icssec.webling.ch
 *   WEBLING_GROUP_ID  – Numeric ID of the "Interessenten" group
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validate(data) {
  const errors = [];
  if (!data.firstName?.trim()) errors.push('firstName');
  if (!data.lastName?.trim()) errors.push('lastName');
  if (!data.email?.trim() || !EMAIL_RE.test(data.email)) errors.push('email');
  if (!data.industry?.trim()) errors.push('industry');
  return errors;
}

const json = (body, status) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });

export async function onRequestPost(context) {
  const { env, request } = context;

  let data;
  try {
    data = await request.json();
  } catch {
    return json({ error: 'Invalid JSON' }, 400);
  }

  /* --- Anti-spam: honeypot --- */
  if (data._hp) {
    return json({ ok: true }, 200);
  }

  /* --- Anti-spam: timing (must wait ≥ 3 s) --- */
  if (typeof data._ts === 'number') {
    const elapsed = Date.now() - data._ts;
    if (elapsed < 3000) {
      return json({ ok: true }, 200);
    }
  } else {
    return json({ ok: true }, 200);
  }

  /* --- Validate required fields --- */
  const missing = validate(data);
  if (missing.length) {
    return json({ error: 'Missing required fields', fields: missing }, 422);
  }

  /* --- Forward to Webling --- */
  const memberPayload = {
    properties: {
      'Vorname': data.firstName.trim(),
      'Name': data.lastName.trim(),
      'E-Mail': data.email.trim(),
      'Industry': data.industry.trim(),
      'Ort': (data.city || '').trim(),
      'Already ISA member?': data.isaMember === true,
    },
    parents: [parseInt(env.WEBLING_GROUP_ID, 10)],
    children: [],
    links: {},
  };

  try {
    const resp = await fetch('https://icssec.webling.ch/api/1/member', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': env.WEBLING_API_KEY,
      },
      body: JSON.stringify(memberPayload),
    });

    if (!resp.ok) {
      const text = await resp.text();
      console.error('Webling error:', resp.status, text);
      return json({ error: 'Registration failed' }, 502);
    }

    return json({ ok: true }, 200);
  } catch (err) {
    console.error('Fetch error:', err);
    return json({ error: 'Service unavailable' }, 503);
  }
}

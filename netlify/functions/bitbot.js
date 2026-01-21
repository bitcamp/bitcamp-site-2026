export async function handler(event) {
    const base = process.env.BITBOT_API_URL
    if (!base) {
        return { statusCode: 500, body: "Missing BITBOT_API_URL" }
    }

    const path = event.path.replace("/.netlify/functions/bitbot", "")
    const qs = event.rawQuery ? `?${event.rawQuery}` : ""
    const upstream = `${base}${path}${qs}`

    const res = await fetch(upstream, {
        method: event.httpMethod,
        headers: {
            "content-type": event.headers["content-type"] || "application/json",
        },
        body: ["GET", "HEAD"].includes(event.httpMethod) ? undefined : event.body,
    })

    const body = await res.text()

    return {
        statusCode: res.status,
        headers: {
            "content-type": res.headers.get("content-type") || "application/json",
        },
        body,
    }
}

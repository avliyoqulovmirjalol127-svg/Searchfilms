// 5 qirrali yulduz chizadi
const star = (cx, cy, R, rot = -90) => {
  const pts = []
  for (let i = 0; i < 10; i++) {
    const r = i % 2 ? R * 0.382 : R
    const a = ((rot + i * 36) * Math.PI) / 180
    pts.push(`${(cx + r * Math.cos(a)).toFixed(2)},${(cy + r * Math.sin(a)).toFixed(2)}`)
  }
  return `<polygon points="${pts.join(' ')}"/>`
}

const svg = (body) =>
  `<svg viewBox="0 0 30 20" preserveAspectRatio="none">${body}</svg>`

// O'zbekiston: 12 yulduz (3 + 4 + 5)
const uzStars = [
  ...[10.5, 12, 13.5].map((x) => star(x, 1.7, 0.55)),
  ...[9.75, 11.25, 12.75, 14.25].map((x) => star(x, 3.1, 0.55)),
  ...[9, 10.5, 12, 13.5, 15].map((x) => star(x, 4.5, 0.55)),
].join('')

export const flags = {
  uz: svg(`
    <rect width="30" height="6.2" fill="#0099b5"/>
    <rect y="6.2" width="30" height="0.6" fill="#ce1126"/>
    <rect y="6.8" width="30" height="6.4" fill="#fff"/>
    <rect y="13.2" width="30" height="0.6" fill="#ce1126"/>
    <rect y="13.8" width="30" height="6.2" fill="#1eb53a"/>
    <circle cx="5" cy="3.1" r="2.2" fill="#fff"/>
    <circle cx="5.8" cy="3.1" r="1.85" fill="#0099b5"/>
    <g fill="#fff">${uzStars}</g>`),

  kaa: svg(`
    <rect width="30" height="7" fill="#2f8fe0"/>
    <rect y="7" width="30" height="0.5" fill="#fff"/>
    <rect y="7.5" width="30" height="5" fill="#f5c518"/>
    <rect y="12.5" width="30" height="0.5" fill="#fff"/>
    <rect y="13" width="30" height="7" fill="#1eb53a"/>
    <circle cx="5" cy="3.5" r="2" fill="#fff"/>
    <circle cx="5.7" cy="3.5" r="1.7" fill="#2f8fe0"/>
    <g fill="#fff">${star(10, 3.5, 1)}</g>`),

  ru: svg(`
    <rect width="30" height="6.7" fill="#fff"/>
    <rect y="6.7" width="30" height="6.6" fill="#0039a6"/>
    <rect y="13.3" width="30" height="6.7" fill="#d52b1e"/>`),

  en: svg(`
    <rect width="30" height="20" fill="#012169"/>
    <path d="M0 0L30 20M30 0L0 20" stroke="#fff" stroke-width="3.4"/>
    <path d="M0 0L30 20M30 0L0 20" stroke="#c8102e" stroke-width="1.5"/>
    <path d="M15 0V20M0 10H30" stroke="#fff" stroke-width="6"/>
    <path d="M15 0V20M0 10H30" stroke="#c8102e" stroke-width="3.4"/>`),

  zh: svg(`
    <rect width="30" height="20" fill="#de2910"/>
    <g fill="#ffde00">
      ${star(5, 5, 3)}
      ${star(10, 2, 1, -75)}
      ${star(12, 4, 1, -50)}
      ${star(12, 7, 1, -20)}
      ${star(10, 9, 1, -45)}
    </g>`),
}
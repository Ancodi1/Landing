import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
	const baseUrl = site ?? new URL('https://ancodi1.github.io/Landing/');
	const homeUrl = new URL('', baseUrl);
	const lastModified = new Date().toISOString().split('T')[0];
	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${homeUrl.href}</loc>
    <lastmod>${lastModified}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml; charset=utf-8' }
	});
};

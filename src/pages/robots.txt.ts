import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
	const basePath = `${import.meta.env.BASE_URL.replace(/\/+$/, '')}/`;
	const siteUrl = site ?? new URL('https://ancodi1.github.io');
	const baseUrl = new URL(basePath, siteUrl);
	const sitemapUrl = new URL('sitemap.xml', baseUrl);

	return new Response(`User-agent: *\nAllow: /\n\nSitemap: ${sitemapUrl.href}\n`, {
		headers: { 'Content-Type': 'text/plain; charset=utf-8' }
	});
};

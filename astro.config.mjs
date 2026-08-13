// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: process.env.PUBLIC_SITE_URL || 'https://www.angelcollazo.com',
	base: process.env.PUBLIC_BASE_PATH || '/'
});

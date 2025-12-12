// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://waveform-analytics.github.io',
	base: '/spec-driven-site',
	integrations: [
		starlight({
			title: 'Spec-Driven Science',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/Waveform-Analytics/spec-driven-site' }],
			components: {
				Footer: './src/components/Footer.astro',
			},
			sidebar: [
				{
					label: 'Get Started',
					items: [
						{ label: 'Overview', slug: 'get-started' },
						{ label: 'Scaffold a Project', slug: 'get-started/scaffold' },
						{ label: 'Your First Spec', slug: 'get-started/first-spec' },
					],
				},
				{
					label: 'Guides',
					items: [
						{
							label: 'The Method',
							autogenerate: { directory: 'guides/method' },
						},
						{
							label: 'AI Collaboration',
							autogenerate: { directory: 'guides/ai' },
						},
						{
							label: 'Examples',
							autogenerate: { directory: 'guides/examples' },
						},
					],
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
		}),
	],
});
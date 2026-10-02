export interface ProjectScreenshot {
	src: string;
	alt: string;
	caption: string;
	width: number;
	height: number;
}

// General feature categories verified against the local module; keep implementation private.
// Public presentation only. Do not import module source code or private assets here.
export const securityModule = {
	title: 'Security Module for PrestaShop',
	status: 'Final testing / Pre-release',
	introduction: 'Módulo de ciberseguridad desarrollado desde cero para PrestaShop, orientado a mejorar la protección del acceso de clientes en tiendas online.',
	technologies: ['PrestaShop', 'PHP', 'MySQL', 'JavaScript', 'HTML', 'CSS'],
	features: [
		{ title: 'Integración nativa con PrestaShop', description: 'Funcionalidades integradas en el acceso y el área de cliente de la tienda.' },
		{ title: 'Configuración desde Back Office', description: 'Panel de configuración para administrar el módulo desde el entorno habitual de la tienda.' },
		{ title: 'Arquitectura modular', description: 'Organización del desarrollo en componentes con responsabilidades diferenciadas.' },
		{ title: 'Persistencia mediante tablas propias', description: 'Gestión de la información del módulo sin modificar la estructura de las tablas core de PrestaShop.' },
		{ title: 'Instalación y desinstalación controlada', description: 'Gestión del ciclo de vida del módulo y de sus recursos propios.' },
		{ title: 'Diseño orientado a seguridad', description: 'Desarrollo centrado en la protección del acceso de clientes y su integración con la tienda.' }
	],
	// Add only real, reviewed screenshots. Paths are relative to public/.
	screenshots: [
		{
			src: 'imx/prestashop-security-module/modulo1.png',
			alt: 'Área de cliente de PrestaShop con la opción de activar y gestionar el acceso biométrico en escritorio',
			caption: 'Integración del módulo en el área de cliente de la tienda.',
			width: 1356,
			height: 529
		},
		{
			src: 'imx/prestashop-security-module/modulo3.png',
			alt: 'Panel de configuración del acceso biométrico en el Back Office de PrestaShop con datos de prueba',
			caption: 'Configuración del módulo desde Back Office en un entorno de pruebas.',
			width: 1680,
			height: 614
		},
		{
			src: 'imx/prestashop-security-module/modulo2.png',
			alt: 'Vista móvil del área de cliente de PrestaShop para activar y gestionar el acceso biométrico',
			caption: 'Interfaz del módulo en el área de cliente desde un dispositivo móvil.',
			width: 390,
			height: 492
		}
	] satisfies ProjectScreenshot[]
};

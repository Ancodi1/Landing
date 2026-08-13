# Portfolio de Ángel Collazo Díaz

Landing personal orientada a presentar servicios de desarrollo web, marketing digital y diseño, junto con una selección de proyectos y trabajos audiovisuales.

El sitio está desarrollado con Astro y prioriza el rendimiento, la adaptación a distintos dispositivos, la accesibilidad y el posicionamiento orgánico.

## Vista online

[www.angelcollazo.com](https://www.angelcollazo.com/)

## Características

- Presentación profesional de servicios, conocimientos y habilidades.
- Portfolio de proyectos de desarrollo web, diseño y marketing digital.
- Galería de banners, flyers y piezas audiovisuales.
- Carruseles de vídeo e imágenes con controles accesibles.
- Diseño responsive para móvil, tablet y escritorio.
- Descarga directa del currículum en PDF.
- Metadatos Open Graph y Twitter Cards.
- Datos estructurados de Schema.org.
- Generación dinámica de `robots.txt` y `sitemap.xml`.

## Tecnologías

- [Astro 6](https://astro.build/)
- HTML5
- CSS3
- JavaScript
- TypeScript

## Requisitos

- Node.js 22.12.0 o una versión posterior.
- npm.

## Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/Ancodi1/Landing.git
cd Landing
npm install
```

Inicia el servidor de desarrollo:

```bash
npm run dev
```

La aplicación estará disponible, por defecto, en `http://localhost:4321/`.

## Comandos disponibles

| Comando | Descripción |
| --- | --- |
| `npm run dev` | Inicia el servidor local con recarga automática. |
| `npm run build` | Genera la versión de producción en `dist/`. |
| `npm run preview` | Sirve localmente la versión de producción. |
| `npm run astro -- <comando>` | Ejecuta comandos de la CLI de Astro. |

## Estructura del proyecto

```text
.
├── public/                 # Recursos estáticos, vídeos, imágenes y CV
├── src/
│   ├── assets/             # Recursos procesados por Astro
│   ├── components/         # Componentes de la interfaz
│   ├── imx/                # Imágenes importadas por los componentes
│   ├── layouts/            # Layout principal y metadatos SEO
│   └── pages/              # Páginas y endpoints del sitio
├── astro.config.mjs        # Configuración de Astro y URL pública
├── package.json            # Dependencias y scripts
└── tsconfig.json           # Configuración de TypeScript
```

## Configuración

El dominio y la ruta base se configuran mediante `PUBLIC_SITE_URL` y `PUBLIC_BASE_PATH`. Si no se definen, el proyecto utiliza `https://www.angelcollazo.com` y la ruta `/` incluidos en `astro.config.mjs`.

Ejemplo para generar el sitio con otro dominio:

```bash
PUBLIC_SITE_URL=https://www.ejemplo.com PUBLIC_BASE_PATH=/ npm run build
```

Esta URL se utiliza para construir las direcciones canónicas, el sitemap, los metadatos sociales y los datos estructurados.

## Despliegue

Antes de publicar una nueva versión, genera y revisa la compilación de producción:

```bash
npm run build
npm run preview
```

El contenido resultante de `dist/` puede desplegarse en cualquier servicio compatible con sitios estáticos, como GitHub Pages, Netlify, Vercel o Cloudflare Pages.

## Autor

Ángel Collazo Díaz

- [GitHub](https://github.com/Ancodi1)
- [LinkedIn](https://www.linkedin.com/in/%C3%A1ngel-collazo-d%C3%ADaz-4896742a9/)

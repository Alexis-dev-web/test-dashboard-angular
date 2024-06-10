# Stage 1: Build
FROM node:22.2-alpine AS build
# Directorio donde se mantendran los archivos de la app
WORKDIR /usr/src/app
# Copiar el package.json y el package-lock en nuestro WORKDIR
COPY package*.json ./
# Instalar dependencias
RUN npm install --force
# Copiar todos los archivos
COPY . .
# Construir la aplicacion lista para produccion, puede no incluir el # flag --prod
RUN npm run build --prod

RUN ls -la /usr/src/app/dist/dashboard-angular
# Angular app construida, la vamos a hostear un server production, este es Nginx

FROM nginx:alpine

# Copiar desde la "Etapa" build el contenido de la carpeta build/
# dentro del directorio indicado en nginx
COPY --from=build /usr/src/app/dist/dashboard-angular/browser /usr/share/nginx/html
# Copiar desde la "Etapa" build el contenido de la carpeta la 
# configuracion de nginx dentro del directorio indicado en nginx
COPY --from=build /usr/src/app/nginx/nginx.conf /etc/nginx/conf.d/default.conf 

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
# EXPOSE 80
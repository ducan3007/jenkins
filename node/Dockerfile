FROM node:18.15.0-slim as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

FROM node:18.15.0-slim as runtime
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["npm", "start"]




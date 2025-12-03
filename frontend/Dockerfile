FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN if [ -f package-lock.json ]; then npm ci; elif [ -f pnpm-lock.yaml ]; then npm i -g pnpm && pnpm i; elif [ -f yarn.lock ]; then yarn install --frozen-lockfile; else npm i; fi
COPY . .
# Build with Vite, VITE_API_URL can be provided at build time
ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=build /app /app
EXPOSE 5173
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "5173"]

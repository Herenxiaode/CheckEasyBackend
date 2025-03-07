# FROM node:20-alpine AS builder
# WORKDIR /app
# COPY ./package.json /app/package.json
# COPY ./bin /app/bin

FROM python:3.13-alpine
# WORKDIR /app
# COPY --from=builder /app /app
# RUN apk update && apk upgrade && rm -rf /var/cache/apk/*
RUN pip install fastapi uvicorn pymysql

# EXPOSE 80
# EXPOSE 443
# CMD ["npm","start"]
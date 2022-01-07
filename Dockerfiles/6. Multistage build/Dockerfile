FROM ubuntu:18.04 as base
WORKDIR /app
RUN echo "Hello World from multistage build" > /app/hello.txt
RUN echo "Hello World from multistage build2" > /app/hello2.txt
RUN echo "Hello World from multistage build3" > /app/hello3.txt
RUN echo "Hello World from multistage build3" > /app/hello4.txt
RUN echo "Hello World from multistage build4" > /app/hello5.txt

FROM alpine:latest
COPY --from=0 /app/*.txt /

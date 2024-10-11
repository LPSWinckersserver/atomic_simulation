# frontend/Dockerfile

# Stage 1: Build the frontend with Rust and Trunk
FROM rust:1.76.0 AS builder

# Install necessary tools: Trunk and wasm-bindgen-cli
RUN cargo install trunk wasm-bindgen-cli --locked

# Add the wasm32 target for compiling to WebAssembly
RUN rustup target add wasm32-unknown-unknown

# Set the working directory
WORKDIR /app

# Cache dependencies by copying Cargo.toml and Cargo.lock first
COPY Cargo.toml Cargo.lock ./

# Create a dummy src/main.rs to build dependencies
RUN mkdir src
RUN echo "fn main() { println!(\"Placeholder\"); }" > src/main.rs

# Build dependencies
RUN cargo build --release
RUN rm src/main.rs

# Copy the actual source code
COPY src/ ./src/
COPY static/ ./static/

# Build the frontend using Trunk
RUN trunk build --release

# Stage 2: Serve the frontend using Nginx
FROM nginx:alpine

# Copy the built frontend from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

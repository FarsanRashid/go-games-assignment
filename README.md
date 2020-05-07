# Game store
Game store is a simple service that exposes single endpoint to quey available games. Games are categorized and client can optionally add category as a filter.

## Endpoint
Exposes single endpoint `/games/` that returns available games in a HTML page. When deployed locally, try
`http://127.0.0.1:8000/games/?category_id=1` 

# Deployment
Clone the repository and follow standard procedure to start development server for django application. Don't forget `pip install -r requirements.txt`.

# Place of improvement/ Concerns
- Dockerize the app
- Write logs in file
- Add profiling
- Use generic view though html rendering in DRF generic views is not obvious as it is designed to serve JSON

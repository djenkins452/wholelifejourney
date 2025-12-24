## Railway Migrations

- Railway does NOT auto-run migrations
- Data migrations must be run explicitly
- Use temporary Start Command:
  python manage.py migrate && ...
- Revert immediately after success

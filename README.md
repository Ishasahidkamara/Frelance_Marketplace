# Freelancer Marketplace Management System

A complete, professional freelance marketplace built with Python/Django connecting skilled freelancers with clients.

## Features

- **Three user roles**: Admin, Freelancer, Client
- Role-based dashboards and access control
- Freelancer profiles with skills, experience, education, portfolio
- Service advertisements with admin approval workflow
- Public marketplace with search and filters
- Project request system (Pending → Active → Submitted → Completed)
- Internal messaging system
- Notification system
- Review and rating system
- Reporting system
- REST API with JWT authentication
- Responsive Bootstrap 5 design

## Tech Stack

- **Backend**: Python 3.11+, Django, Django REST Framework
**Currency**: Sierra Leonean Leone (NLe) — all prices, budgets and rates are in NLe.
- **Frontend**: Bootstrap 5, Bootstrap Icons, JavaScript, Chart.js
- **Auth**: Django auth + JWT (DRF Simple JWT)

## Installation

### 1. Clone / navigate to the project

```bash
cd freelancer_marketplace
```

### 2. Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Seed sample data

```bash
python manage.py seed_data
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

## Default Accounts

| Role       | Username     | Password   |
|------------|--------------|------------|
| Admin      | admin        | Admin@123  |
| Freelancer | john_dev     | Pass@1234  |
| Freelancer | jane_design  | Pass@1234  |
| Freelancer | mike_mobile  | Pass@1234  |
| Freelancer | sarah_write  | Pass@1234  |
| Client     | mary_client  | Pass@1234  |
| Client     | alex_client  | Pass@1234  |
| Client     | linda_client | Pass@1234  |

## Project Structure

```
freelancer_marketplace/
├── config/          # Django settings and URLs
├── accounts/        # Custom User model, auth views
├── freelancers/     # Freelancer profiles
├── clients/         # Client profiles
├── services/        # Service advertisements + categories
├── projects/        # Project requests and management
├── messaging/       # Internal messaging
├── reviews/         # Reviews and ratings
├── notifications/   # Notification system
├── reports/         # Reporting system
├── dashboard/       # Admin/Freelancer/Client dashboards
├── api/             # REST API endpoints
├── templates/       # HTML templates
├── static/          # CSS, JS, images
└── media/           # User uploads
```

## REST API

Base URL: `/api/`

- `POST /api/auth/token/` — obtain JWT token
- `POST /api/auth/token/refresh/` — refresh token
- `GET /api/services/` — list approved services
- `GET /api/freelancers/` — list freelancer profiles
- `GET /api/categories/` — list categories
- `GET /api/projects/` — list user's projects
- `POST /api/projects/{id}/accept/` — accept project (freelancer)
- `POST /api/projects/{id}/complete/` — confirm completion (client)
- Full CRUD on: users, services, projects, reviews, notifications, reports, messages

## Complete Workflow

1. Freelancer registers → creates profile → adds skills
2. Freelancer creates service → Admin approves
3. Client registers → searches marketplace → views service
4. Client sends project request → Freelancer accepts
5. Both communicate via messaging
6. Freelancer submits work → Client confirms completion
7. Client leaves review → Freelancer rating updates
8. Admin monitors everything from dashboard

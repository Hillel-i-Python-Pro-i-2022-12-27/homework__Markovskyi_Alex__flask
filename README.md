This is a first program with Makefile+Docker.

For starting application use terminal command:



# Init environment for developer
make init-dev



# Run application
make homework-i-run

# Delete all packages 
make homework-i-purge

# Run tools for files from commit
make pre-commit-run

# Run tools for all from commit
make pre-commit-run-all




--== RUN APPLICATION WITH DOCKER ==--

# Make all actions needed for run homework from zero.
make d-homework-i-run

# Make all actions needed for purge homework related data.
make d-homework-i-purge

# Just run.
make d-run

# STOP service.
make d-stop

# Purge all data related with services.
make d-purge:
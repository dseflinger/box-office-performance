# PostgreSQL Database Schema Overview
## Theaters (boxoffice_theater)
Stores information about each theater
Fields
- **id:** Primary Key
- **name:** Name of theater
- **location:** Location of theater
- **num_screens:** Number of screens in theater
- **capacity:** Capacity of theater
  
## Theaters (boxoffice_movie)
Stores information about each theater
Fields
- **id:** Primary Key
- **name:** Name of Movie
- **genre:** Genre of Movie (action, comedy, drama, horror, romance, scifi, documentary)
- **release_date:** Release date of Movie
- **duration_minutes:** Duration in minutes of movie

## Sales (boxoffice_sale)
Stores information about each theater
Fields
- **id:** Primary Key
- **theater:** Foreign Key to theater
- **movie:** Foreign Key to movie
- **date:** Date of Sale
- **tickets_sold:** Number of tickets sold
- **amount:** Revenue for that movie/theater/date

## Design Notes
I chose to add movie and theater as foreign key references in the **boxoffice_sale** table because it 
represents the relationship between a movie, a theater, and a specific sale date. 
Deleting a movie or theater from the database also removes and sales referencing those. 
I wanted to avoid data duplication and keep relationships clear, so while sale entries are dependent 
on movie and theater records, they don't need to reference each other.

Quick and dirty course management system.

Some notes:

There were several unclear parts in the spec.  The "show all" and "search" API weren't clear on what they should
return; the other APIs often weren't clear on how their targets should be specified.  I went with the simplest
answer in most cases on account of limited time, but naturally in reality I'd ask for a clarification.

It was also unclear what "search by date" meant; I went with the simplest answer (exact match).

The most important missing piece, though, was the lack of any clear way to register students to courses.
I added an API for that, even though it wasn't requested, since without it there was no way to test the relevant relation.

I would say I spent roughly equal amounts of time on each part, in terms of understanding, designing, coding, and testing.
Normally I would probably spend more time on design and testing (measure twice, cut once), but time was tight!


If I had more time or resources, the first thing I'd do is add more error-checking for invalid inputs.
I'd also expand the search-by-date functionality to search before, after, between two dates, etc.

Note that the search student and show courses for student endpoint are the same (it returns all students of that name, plus all courses), due to the ambiguity in terms of how students should be identified and what the search-by-title API should return.
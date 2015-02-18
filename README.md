# framer-iterations
Structure for publishing Framer.js iterations (based on/taken from the http://examples.framerjs.com website)

To use, clone the repo, then add `projects.framer` in the `static/iterations` directory.  Then run `make` to compile the Coffeescript.  Everything should then be able to be uploaded.  There is a `deploy.php` script that works on (mt) at the least; you can clone into your html directory then hit `http://domain.com/deploy.php` with a Github webhook.

Broken: mobile navigation (to be able to navigate between the different iterations), 1x/2x switching (on the desktop)

Todo: better deployment (index.html could be updated based on `projects.framer`)

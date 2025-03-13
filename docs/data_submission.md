# Data Submission Portal

| This app uses HTMX as front-end so it will utilize more components than needed to utilize the fetures of HTMX

[Return to the main documentation](documentation.md)

### App Workflow
- Visiting /submission_portal will give you the home page of the app
- The top pane just below the navbar presents a total available data for both `text` and `image_url`
- The available data will be paginated across multiple pages with pagination down below the page (The available data entry for each page is 10)
- The search bar will return the result yielding every data that your search contains
- Filtering category between Text, Image_URl and All (Both Text and Image_URL) will filter respectively
- Use the `+` button on the right most side of the table header row to add more
- Pagination will behave accordingly towards searched result and filtered data

### Templates
- `submission_page.html` extends the navbar from `index.html` and contains the basic structure such as <b>table headers, a search bar, the top pane for total available data, and buttons for filtering and adding data</b>
- `components` include other necessary `.html`
    - `is_reviewed.html` is used for <i>reviewed/unreviewed</i> feature in the app
    - `pagination.html` actualizes the implementation of pagination across different functions
    - `submission_form.html` provides a form to add new data
    - `submission_table.html` provides a table-only data that will be replaced when being filtered or searched

### models.py
- Contains DataEntry model with 5 main fields
    - `content`
        - A text field that will contain the main content of the data entry object
    - `category`
        - A character field whose available values are 'Text' and 'Image URL'
    - `is_reviewed`
        - A boolean field that will record the entry as being reviewed or not
    - `updated`
        - A Date-Time Field that will record the updated time as the data of the entry is being changed
    - `created`
        - A Date-Time Field that will record the created date and time of the entry

### utils.py
- Function `paginate`
    - args
        - data -> the data it will try to paginate
        - request -> the request that will be passed to the function so it can request."GET".get the page of the request from the pagination
        - per_page -> 10 items will be shown on each page of the pagination unless otherwise specified

### views.py
- Function `submission_portal`
    - the main function that will deliver all the objects as well as the total number of each object category towards the webpage
- Function `form_search`
    -  the handler for the search bar which will return paginated queried result with appropriate template
- Function `form_filter_category`
    - the category filter handler which will return filtered data between image_url and text or both as user specifies
- Function `handle_reviewed`
    - the function to quickly change the status of the review which will also reflect on the front end via htmx without the page reload
- Function `form_add`
    - provides a form to submit a new data to the django database

### urls.py
| Since this resides under /submission_portal/* via root `urls.py`, the paths specified will be `/submission_portal/*`
- path `''`
    - URL -> /submission_portal/
    - this will retrieve the template, data from views.submission_portal
- path `form_add`
    - URL -> /submission_portal/form_add/
    - this will provide a form to add new data
- path `form_filter-category`
    - URL -> /submission_portal/form_filter_category
    - this will be used upon filtering data by category and upon pagination on the filtered data
- path `search_result`
    - URL -> /submission_portal/search_result
    - this will be used upon searching data and upon pagination on the queried results
- path `handle_reviewed`
    - URL -> /submission_portal/handle_reviewed
    - this will be called whenever a `is_reviewed` status is switched
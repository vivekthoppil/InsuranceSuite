## Primary Goal

We would like to see you come up with a solution that allows insurers to define their own custom data model for their risks. There should be no database tables called `automobiles`, `houses`, or `prizes`. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

### Data

For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. Field types should be either `text`, `number`, `date`, or `enum` (where there are multiple potential options but only one choice can be made).

Deliverables will be either...

1. A Python file containing the ORM classes for these tables.
2. An entity relationship diagram, which depicts the tables and their relationship to one another.
3. Both 1 and 2, because you're awesome.

### Backend

For the backend, create two API endpoints. One that returns a single risk type and one that returns a list of all risk types. Include all of the risk types' fields, field types, and any other data about the fields. This is your chance to show that you know how to create clean REST APIs.

Deliverables will be...

1. A well-tested REST API written in Python.

### Frontend

The frontend is all about collecting information as it relates to these generic models. Create a single page that hits your risk type API endpoint(s) and displays all of the fields to the user in a form. Be sure to display at least one field of each type on the page. Don't worry about submitting the form.

Fields should use appropriate widgets based on their type. `text` fields should display as text boxes, `date` fields should use date pickers, and so on.

Deliverables will be...

1. A modern JavaScript app. **Bonus points** if you use ES6 and a modern JavaScript framework. **Mega bonus points** if you use Vue.js specifically.

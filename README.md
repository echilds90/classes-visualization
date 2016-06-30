d

### Prerequisites

We also use a number of node.js tools to initialize and test classes-visualization. You must have node.js and
its package manager (npm) installed.  You can get them from [http://nodejs.org/](http://nodejs.org/).

### Install Dependencies

```
npm install
```

*Note that the `bower_components` folder would normally be installed in the root folder but
classes-visualization changes this location through the `.bowerrc` file.  Putting it in the app folder makes
it easier to serve the files by a webserver.* (https://github.com/angular/angular-seed)

### Run the Application

####Start Server
```
npm start
```

Now browse to the app at `http://localhost:8000/index.html`.



### Running Unit Tests

Run test runner, this will continue to run as the code changes

```
npm test
```

For non continuous testing use

```
npm run test-single-run
```


### End to end testing

start the app to run tests against it

```
npm start
```

install the web driver

```
npm run update-webdriver
```

run the tests

```
npm run protractor
```

This script will execute the end-to-end tests against the application being hosted on the
development server.


## Updating Angular

update node
```
npm update
```

update angular

```
bower update
```

## Sources

https://github.com/angular/angular-seed
https://www.codementor.io/angularjs/tutorial/angularjs-calendar-directives-less-cess-moment-font-awesome

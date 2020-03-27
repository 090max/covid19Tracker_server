

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Covid 19 Tracker</h3>

  <p align="center">
   A pyhton flask API that regularly tracks Covid19 cases in India. 
    <br />
    <a href="http://covidtracker19.herokuapp.com/">View Demo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Routes Information](#routes-information)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)




<!-- ABOUT THE PROJECT -->
## Routes Information

* /getgeneral : Returns a JSON data of the current cases report of India.
* /getanalytics : Returns a JSON data of the past case report along with current cases in India .This is specifically for data visualization.
* /getstate?state=<statename> :Return a JSON data of the current case report of a particular state.
* /getstate?state=all :Return a JSON data of the current case report of all Indian states.

### Built With
* [ReactJS](https://reactjs.org/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)


<!-- GETTING STARTED -->
## Getting Started

Here is a quick installation guide.

### Prerequisites

* npm
```sh
npm install npm@latest -g
```

### Installation

To download it as a Personalize Web App , open the <a href="https://covid19indiatracker.netlify.com">Link</a> in Google Chrome and then "Add to home screen".To Run the application for development Do the following:
1. To Run the application for development ,Clone the repo
```sh
git clone https://github.com/090max/covid19IndiaTracker
```
2. Install NPM packages.
```sh
npm i
```
4. Run the client.`
```JS
npm start
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FeatureBranch`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/FeatureBranch`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<<<<<<< HEAD
Hubspot Web

### What is it ?

The idea for Project Hubspot is a simple one. Allow cafe’s, events and any organizations that have internet to simply plug in a device that they can easily control online and start selling internet access for extra profit with various options to choose from with the easy to use management interface.

### And this Repo ?

This repo contains our online application that runs on App Engine.

The website handles all purchases as well as any web traffic we receive to the website.


### How is this all setup ?

The infrastructure runs on App Engine and is built locally using Grunt to manage all the tasks.

Currently we have the folllowing tasks setup for us:

* <strong>clean</strong>: Will clean all the tmp and dist directories. We run this ourselves when you are doing a release 'build'
* <strong>compile</strong>: Compiles all the scripts and styles under assets/ which are in either coffeescript or less to css and the public/dist folder.
* <strong>build</strong>: Runs a <strong>clean</strong> and <strong>compile</strong>. But then also takes those files and produces minified versions of it. The command also saves a new <strong>dist_rev</strong>. In the projects <pre>app.yaml</pre>.
* <strong>test</strong>: Runs all our local tests in test/
* <strong>deploy</strong>: Runs a <strong>build</strong>, <strong>test</strong> and then runs the app engine deploy command. This will then send the local new version up to app engine and will be serving in a few seconds. <strong style="color:red;">The site will not be deployed if the tests don't pass</strong> and we log all deploys so we know when what is happening</strong>

### Running Locally

The project uses Grunt (http://gruntjs.com/) so first things first. Do you have nodejs & grunt installed ? If not see http://nodejs.org/ & http://gruntjs.com/getting-started.

When you have grunt setup there is a quick setup script that is provided to get you running quickly. 

`````
./setup.sh
`````

When the setup is done the project should now be runnable. To start the server you need to execute:

`````
grunt run
`````

The webserver will now be running on <strong>8080</strong> and the grunt will be watching and recompling the local files in case they change.

### Deploying

To deploy the site grunt and NodeJS is required again. Please see <a href="#Running Locally">Running Locally</a>. When that's setup you can continue.

To deploy we created a local Grunt task that can just be run and the project will compile, minify all assets and upload to app engine, which I assume you have access to as you are accessing this README.

### License

Copyright 2013 Johann du Toit
All Rights Reserved.

NOTICE:  All information contained herein is, and remains the property of Lusahn CC and its suppliers, if any.  The intellectual and technical concepts contained herein are proprietary to Lusahn CC and its suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.

Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from Johann du Toit.


=======
# IdentiChip

After I wrote the Microchip Website I saw that most the Microchip world is very fragmented. To Search for a Microchip you have to got to all the Providers and type in the Chip Number. So I thought why not build a central point for this all to happen.

I'm currently writing this and hope to have code soon. It's basicly a Google for Microchip Providers. A Users types in a Microchip number and I search all the providers that registered and implemented my API for the chip. One Stop Search for all Microchips. I'm also giving Assocations that need this information the change to register and access the info from the providers giving users and breed associations access to a one stop site to manage all their information.

Microchip Providers Integrate with the system by opening up a certain url that will expose the data to the server for a search.

## Presentations

Going to be doing a presentation on the Site on the 27th of October in Cape Town. Any interested feel free to join.

## Running

Running the system is not quite that difficult.

All you need is the source and Google App Engine Local Dev Server.

Checkout a Copy of our Source and then run the Directory in the Local App Engine Server:

	$ dev_appserver.py IdentiChip/

Visit localhost:8080 and you should be ready to go. Note the port can differ on diffrent platforms. That's just the default on OSX.

## API

The service offers a API that the user can use to search for microchips.

View the Documentation for the API at http://www.identichip.org/developer

## Contributors

* Johann du Toit

## License

(MIT License)

Copyright (c) 2012 Johann du Toit

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>>>>>>> adb57e737fc1bbaf3bb404a1589801d4c5666da5

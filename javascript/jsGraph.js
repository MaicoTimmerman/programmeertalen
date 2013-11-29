/*
 * JavaScript Function Plotting
 *
 * This code is from http://www.html5canvastutorials.com/labs/html5-canvas-graphing-an-equation/
 * but removed from the html file itself and put in a .js file. The html file in which we want
 * plot functions should 'include' this file by using the line:
 *   <script src='jsGraph.js'></script>
 * in the <head> ... </head> section of the html file
 */

/* Constructor for a Graph canvas*/
function Graph(config) {
    console.log(this);

    /* user defined properties */
    this.canvas = document.getElementById(config.canvasId);
    this.minX = config.minX;
    this.minY = config.maxY;
    this.maxX = config.maxX;
    this.maxY = config.minY;
    this.unitsPerTick = config.unitsPerTick;

    /* constants */
    this.axisColor = '#aaa';
    this.font = '8pt Calibri';
    this.tickSize = 20;

    /* relationships */
    this.context = this.canvas.getContext('2d');
    this.rangeX = this.maxX - this.minX;
    this.rangeY = this.minY - this.maxY;
    this.unitX = this.canvas.width / this.rangeX;
    this.unitY = this.canvas.height / this.rangeY;
    this.centerY = Math.round(Math.abs(this.minY / this.rangeY) * this.canvas.height);
    this.centerX = Math.round(Math.abs(this.minX / this.rangeX) * this.canvas.width);
    this.iteration = (this.maxX - this.minX) / 1000;
    this.scaleX = this.canvas.width / this.rangeX;
    this.scaleY = this.canvas.height / this.rangeY;

    /* draw x and y axis */
    this.drawXAxis();
    this.drawYAxis();

}

/* draw the XAxis with the correct ticks */
Graph.prototype.drawXAxis = function() {
    var context = this.context;
    context.save();
    context.beginPath();
    context.moveTo(0, this.centerY);
    context.lineTo(this.canvas.width, this.centerY);
    context.strokeStyle = this.axisColor;
    context.lineWidth = 2;
    context.stroke();

    /* draw tick marks */
    var xPosIncrement = this.unitsPerTick * this.unitX;
    var xPos, unit;
    context.font = this.font;
    context.textAlign = 'center';
    context.textBaseline = 'top';

    /* draw left tick marks */
    xPos = this.centerX - xPosIncrement;
    unit = -1 * this.unitsPerTick;
    while(xPos > 0) {
        context.moveTo(xPos, this.centerY - this.tickSize / 2);
        context.lineTo(xPos, this.centerY + this.tickSize / 2);
        context.stroke();
        context.fillText(unit, xPos, this.centerY + this.tickSize / 2 + 3);
        unit -= this.unitsPerTick;
        xPos = Math.round(xPos - xPosIncrement);
    }

    // draw right tick marks */
    xPos = this.centerX + xPosIncrement;
    unit = this.unitsPerTick;
    while(xPos < this.canvas.width) {
        context.moveTo(xPos, this.centerY - this.tickSize / 2);
        context.lineTo(xPos, this.centerY + this.tickSize / 2);
        context.stroke();
        context.fillText(unit, xPos, this.centerY + this.tickSize / 2 + 3);
        unit += this.unitsPerTick;
        xPos = Math.round(xPos + xPosIncrement);
    }
    context.restore();
};

/* draw the YAxis with the correct ticks */
Graph.prototype.drawYAxis = function() {
    var context = this.context;
    context.save();
    context.beginPath();
    context.moveTo(this.centerX, 0);
    context.lineTo(this.centerX, this.canvas.height);
    context.strokeStyle = this.axisColor;
    context.lineWidth = 2;
    context.stroke();

    /* draw tick marks */
    var yPosIncrement = this.unitsPerTick * this.unitY;
    var yPos, unit;
    context.font = this.font;
    context.textAlign = 'right';
    context.textBaseline = 'middle';

    /* draw top tick marks */
    yPos = this.centerY - yPosIncrement;
    unit = this.unitsPerTick;
    while(yPos > 0) {
        context.moveTo(this.centerX - this.tickSize / 2, yPos);
        context.lineTo(this.centerX + this.tickSize / 2, yPos);
        context.stroke();
        context.fillText(unit, this.centerX - this.tickSize / 2 - 3, yPos);
        unit += this.unitsPerTick;
        yPos = Math.round(yPos - yPosIncrement);
    }

    /* draw bottom tick marks */
    yPos = this.centerY + yPosIncrement;
    unit = -1 * this.unitsPerTick;
    while(yPos < this.canvas.height) {
        context.moveTo(this.centerX - this.tickSize / 2, yPos);
        context.lineTo(this.centerX + this.tickSize / 2, yPos);
        context.stroke();
        context.fillText(unit, this.centerX - this.tickSize / 2 - 3, yPos);
        unit -= this.unitsPerTick;
        yPos = Math.round(yPos + yPosIncrement);
    }
    context.restore();
};

/* This method draws the equation in the given color and thickness.
 * Ignores the asymptote xva while drawing
 */
Graph.prototype.drawEquation = function(equation, color, thickness, xva) {
    var context = this.context;
    context.save();
    context.save();
    this.transformContext();

    context.beginPath();
    context.moveTo(this.minX, equation(this.minX));

    /* Actual drawing of the graph */
    for(var x = this.minX + this.iteration; x <= this.maxX; x += this.iteration) {
        if (Math.abs(x - xva) > 0.00001 || xva === undefined)  {
            context.lineTo(x, equation(x));
        }
        else {
            context.moveTo(xva + this.iteration,equation(xva + this.iteration));
        }
    }

    context.restore();
    context.lineJoin = 'round';
    context.lineWidth = thickness;
    context.strokeStyle = color;
    context.stroke();
    context.restore();
};

/* Transform the context of the canvas to put the origin in the middle of the canvas */
Graph.prototype.transformContext = function() {
    var context = this.context;

    /* move context to center of canvas */
    this.context.translate(this.centerX, this.centerY);

    /*
     * stretch grid to fit the canvas window, and
     * invert the y scale so that that increments
     * as you move upwards
     */
    context.scale(this.scaleX, -this.scaleY);
};

/* Conbined function to plot the graph and find the zero-point between two given values. */
Graph.prototype.plotFunctionAndZero = function(f,x0,x1,color, thickness, xva) {
    /* draw the graph, with or without asymptote. */
    if (xva === undefined) {
        this.drawEquation(f, color, thickness, xva);
    }
    else {
        this.drawEquation(f, color, thickness);
    }
    var context = this.context;
    context.save();
    context.save();
    this.transformContext();

    /* draw the litte crosses at both x */
    context.beginPath()
    context.moveTo(x0 - 0.1, f(x0) - 0.1);
    context.lineTo(x0 + 0.1, f(x0) + 0.1);
    context.moveTo(x0 - 0.1, f(x0) + 0.1);
    context.lineTo(x0 + 0.1, f(x0) - 0.1);
    context.moveTo(x1 - 0.1, f(x1) - 0.1);
    context.lineTo(x1 + 0.1, f(x1) + 0.1);
    context.moveTo(x1 - 0.1, f(x1) + 0.1);
    context.lineTo(x1 + 0.1, f(x1) - 0.1);
    context.restore();

    context.lineJoin = "round";
    context.lineWidth = thickness;
    context.strokeStyle = "black";
    context.stroke();
    context.restore();

    // TODO make the dissection circle
}

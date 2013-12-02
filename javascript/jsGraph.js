/*
 * Name:    Maico Timmerman
 * CKNUM:   10542590
 * 
 * jsGraph.js:
 *  This script can draw graphs and determine the zeropoint between an interval.
 */


/* Constructor for a Graph canvas. */
function Graph(config) {
    console.log(this);

    /* user defined properties. */
    this.canvas = document.getElementById(config.canvasId);
    this.minX = config.minX;
    this.minY = config.maxY;
    this.maxX = config.maxX;
    this.maxY = config.minY;
    this.unitsPerTick = config.unitsPerTick;

    /* constants. */
    this.axisColor = '#aaa';
    this.font = '8pt Calibri';
    this.tickSize = 20;

    /* relationships. */
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

    /* draw x and y axis. */
    this.drawXAxis();
    this.drawYAxis();

}

/* Draw the XAxis with the correct ticks. */
Graph.prototype.drawXAxis = function() {
    var context = this.context;
    context.save();
    context.beginPath();
    context.moveTo(0, this.centerY);
    context.lineTo(this.canvas.width, this.centerY);
    context.strokeStyle = this.axisColor;
    context.lineWidth = 2;
    context.stroke();

    /* Draw tick marks. */
    var xPosIncrement = this.unitsPerTick * this.unitX;
    var xPos, unit;
    context.font = this.font;
    context.textAlign = 'center';
    context.textBaseline = 'top';

    /* Draw left tick marks. */
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

    /* Draw right tick marks. */
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

/* Draw the YAxis with the correct ticks. */
Graph.prototype.drawYAxis = function() {
    var context = this.context;
    context.save();
    context.beginPath();
    context.moveTo(this.centerX, 0);
    context.lineTo(this.centerX, this.canvas.height);
    context.strokeStyle = this.axisColor;
    context.lineWidth = 2;
    context.stroke();

    /* Draw tick marks. */
    var yPosIncrement = this.unitsPerTick * this.unitY;
    var yPos, unit;
    context.font = this.font;
    context.textAlign = 'right';
    context.textBaseline = 'middle';

    /* Draw top tick marks. */
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

    /* Draw bottom tick marks. */
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
 * Ignores the asymptote xva while drawing.
 */
Graph.prototype.drawEquation = function(f, color, thickness, xva) {
    var context = this.context;
    context.save();
    context.save();
    this.transformContext();

    context.beginPath();
    context.moveTo(this.minX, f(this.minX));

    /* Actual drawing of the graph. */
    var nextXva = 0;
    for(var x = this.minX + this.iteration; x <= this.maxX; x += this.iteration) {
        if (xva === undefined || Math.abs(x - xva[nextXva]) > 0.00001)  {
            context.lineTo(x, f(x));
        }
        else {
            /* BUG: the moveTo function works with a list of one asymptote
             * but using a list with more then 1 asymptote causes both to be
             * drawn line horizontal lines.
             * I have no clue whatsoever causes this to happen.
             */
            context.moveTo(xva + this.iteration,f(xva + this.iteration));
            if (nextXva < xva.length -1) {
                nextXva++;
            }
        }
    }

    context.restore();
    context.lineJoin = 'round';
    context.lineWidth = thickness;
    context.strokeStyle = color;
    context.stroke();
    context.restore();
};

/* Transform the context of the canvas to put the origin in the middle of the canvas. */
Graph.prototype.transformContext = function() {
    var context = this.context;

    /* Move context to center of canvas. */
    this.context.translate(this.centerX, this.centerY);

    /*
     * Stretch grid to fit the canvas window, and
     * invert the y scale so that that increments
     * as you move upwards.
     */
    context.scale(this.scaleX, -this.scaleY);
};

/* Conbined function to plot the graph and find the zero-point between two given values. */
Graph.prototype.plotFunctionAndZero = function(f,x0,x1,color, thickness, xva) {
    /* Draw the graph, with or without asymptote. */
    if (xva !== undefined) {
        this.drawEquation(f, color, thickness, xva);
    }
    else {
        this.drawEquation(f, color, thickness);
    }
    var context = this.context;
    context.save();
    context.save();
    this.transformContext();

    /* Draw the litte crosses at both x. */
    context.beginPath()
    context.moveTo(x0 - 0.1, f(x0) - 0.1);
    context.lineTo(x0 + 0.1, f(x0) + 0.1);
    context.moveTo(x0 - 0.1, f(x0) + 0.1);
    context.lineTo(x0 + 0.1, f(x0) - 0.1);
    context.moveTo(x1 - 0.1, f(x1) - 0.1);
    context.lineTo(x1 + 0.1, f(x1) + 0.1);
    context.moveTo(x1 - 0.1, f(x1) + 0.1);
    context.lineTo(x1 + 0.1, f(x1) - 0.1);

    /* Draw a circle at the zero point. */
    var zero = this.getZero(f, x0, x1);
    context.moveTo(zero, f(zero));
    context.arc(zero, f(zero), 0.1, 0, Math.PI*2, false);

    context.restore();
    context.lineJoin = "round";
    context.lineWidth = 1;
    context.strokeStyle = "black";
    context.stroke();
    context.restore();
}

/* Determine the zero point between the two given x. */
Graph.prototype.getZero = function(f, x0, x1) {
    var i = 1;
    var middle;
    var endA = x0;
    var endB = x1;
    while (i <= this.canvas.width) {
        middle = (endA + endB)/2;
        /* if the middle is exactly zero or lower then 10*the iteration then the zeropoint is found */
        if (f(middle) == 0 || Math.abs((endB - endA)/2) < (this.iteration/10)) {
            return middle;
        }
        i = i + 1;
        /* Check if the sign of x in the middle the same is as the x at endA. */
        if ((f(middle) && f(middle)/Math.abs(f(middle))) == (f(endA) && f(endA)/Math.abs(f(endA)))) {
            endA = middle;
        }
        else {
            endB = middle;
        }
    }
}

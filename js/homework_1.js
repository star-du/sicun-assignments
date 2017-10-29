var canvas;
var ctx;
var color;
var isBlue=false;
var chessData=[];
var i;
for (var x=0;x<10;x++){
    chessData[x]=[];
    for (var y=0;y<10;y++){
        chessData[x][y]=0;
    }
}




function draw() {
  canvas = document.getElementById('canvas');
  if (canvas.getContext)
    ctx = canvas.getContext('2d');
        for(i=0;i<10;i++){
            for(var j=0;j<10;j++)
            ctx.strokeRect(50+50*i,50+50*j,50,50);}

}


function play(e){
    var px = e.clientX - 50;
    var py = e.clientY - 50;
    var x = parseInt(px/50);
    var y = parseInt(py/50);
    console.log('px:'+px+'\n'+'py:'+py)
    if(px<0||py<0||x>9||y>9||chessData[x][y] !=0){
        alert('Invalid move.')
        return;
    }
doCheck(x,y);
}


function doCheck(x,y){
if(isBlue){color='blue';
          chessData[x][y]=2;}
    else{color='red';
        chessData[x][y]=1;}
console.log(color+' at '+x+','+y);
chess(x,y,color);
whoWin(x,y,color);
}


function chess(x,y,color){
    ctx.fillStyle=color;
    ctx.fillRect(50+50*x,50+50*y,50,50);
    isBlue=!isBlue;
}

var counter;
function right(x,y){for(i=x+1;i<=9&&chessData[i][y] == chessData[x][y];i++)counter+=1;}
function left(x,y){for(i=x-1;i>=0&&chessData[i][y] == chessData[x][y];i--)counter+=1;}
function up(x,y){for(i=y+1;y<=9&&chessData[x][i] == chessData[x][y];i++)counter+=1;}
function down(x,y){for(i=y-1;i>=0&&chessData[x][i] == chessData[x][y];i--)counter+=1;}

function left_up(x,y){for(i=1;x-i>=0&&y-i>=0&&chessData[x-i][y-i] == chessData[x][y];i++)counter+=1;}
function right_down(x,y){for(i=1;x+i<=9&&y+i<=9&&chessData[x+i][y+i] == chessData[x][y];i++)counter+=1;}
function left_down(x,y){for(i=1;x-i>=0&&y+i<=9&&chessData[x-i][y+i] == chessData[x][y];i++)counter+=1;}
function right_up(x,y){for(i=1;x+i<=9&&y-i>=0&&chessData[x+i][y-i] == chessData[x][y];i++)counter+=1;}

function whoWin(x,y,color){
    counter=1;
    right(x,y);
    left(x,y);
    console.log('horizonal counter:'+counter);
    if(counter==5) alert('winner is '+color);
    counter=1;
    up(x,y);
    down(x,y);
    console.log('vertical counter:'+counter);
    if (counter==5){alert('winner is '+color);}
    counter=1;
    left_up(x,y);
    right_down(x,y);
    console.log('counter_1:'+counter);
    if (counter==5){alert('winner is '+color);}
    counter=1;
    right_up(x,y);
    left_down(x,y);
    console.log('counter_2:'+counter);
    if (counter==5){alert('winner is '+color);}

}

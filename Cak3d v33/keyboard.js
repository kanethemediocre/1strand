////////////////////////////////////////////////////////Keyboard input/////////////////////////////////////
window.addEventListener("keydown", function (event) {
    if (event.defaultPrevented) {
      return; // Do nothing if the event was already processed
    }
    switch (event.key) { 
  
      case "ArrowDown": 	  
		  cakelevel--;
          if ((cakelevel<0)&&(partclass==0))
              {cakelevel = cakeids.length-1;}
          else if ((cakelevel<0)&&(partclass==1))
              {cakelevel = tcakeids.length-1; }
		  
          freshstagevalues();
            break;
      case "ArrowUp": 
	  
	      cakelevel++;
          if ((cakelevel>=cakeids.length)&&(partclass==0))
              {cakelevel = 0;}
          else if ((cakelevel>=tcakeids.length)&&(partclass==1))
              {cakelevel = 0;}
          freshstagevalues();
            break;		  
      case "q": 
         //Do nothing.
          break;	  
      default:
        return; // Quit when this doesn't handle the key event.
    } //end event key handling switch
    event.preventDefault();// Cancel the default action to avoid it being handled twice
  }, true);	//end of event key handling, not clear what the ", true);" is about	
function toggleRomKan() {
    var wordTag = $("#wordName");
    var current = wordTag.text();
    var next = wordTag.data("toggle");
    wordTag.text(next);
    wordTag.data("toggle", current);
}
$(document).ready(function(){

    // jQuery methods go here...
    
}); 
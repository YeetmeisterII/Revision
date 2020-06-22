// Code modified from W3 Schools example
var current_topic_int = null

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function localDropdown(topic_num) {
    if (!((current_topic_int == null) || (current_topic_int === topic_num))) {
        document.getElementById(`nav_local_content_${current_topic_int}`).classList.remove("show");
    }
    document.getElementById(`nav_local_content_${topic_num}`).classList.toggle("show");
    current_topic_int = topic_num
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    var current_button_clicked = event.target.matches(`#nav_local_button_${current_topic_int}`);
    var topic_is_null = current_topic_int == null

    if (!(current_button_clicked || topic_is_null)) {
        document.getElementById(`nav_local_content_${current_topic_int}`).classList.remove("show");
        current_topic_int = null

    }
}
document.addEventListener('DOMContentLoaded', function() {
  var fadeInSection = function() {
    var sections = document.querySelectorAll('.fade-in');
    sections.forEach(function(section) {
      if (section.getBoundingClientRect().top - window.innerHeight < 0) {
        section.classList.add('is-visible');
      }
    });
  };
  fadeInSection();
  window.addEventListener('scroll', fadeInSection);
});

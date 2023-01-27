
// ===== Counting Meter ===== /////

class CountUp {
    constructor(triggerEl, counterEl) {
      const counter = document.querySelector(counterEl);
      const trigger = document.querySelector(triggerEl);
      let num = 0;
  
      const countUp = () => {
        if (num <= counter.dataset.stop) ++num;
        counter.textContent = num;
      };
  
      const observer = new IntersectionObserver(
        (el) => {
          if (el[0].isIntersecting) {
            const interval = setInterval(() => {
              num < counter.dataset.stop ? countUp() : clearInterval(interval);
            }, counter.dataset.speed);
          }
        },
        { threshold: [0] }
      );
  
      observer.observe(trigger);
    }
  }
  
  // Initialize any number of counters:
  new CountUp("#start1", "#counter1");
  new CountUp("#start2", "#counter2");
  
  
  
  
  // ===== Counting Meter ===== /////
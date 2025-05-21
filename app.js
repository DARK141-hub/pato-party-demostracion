
  const canvas = document.getElementById('confettiCanvas');
  const ctx = canvas.getContext('2d');
  let W = window.innerWidth;
  let H = window.innerHeight;
  let mp = 150; // Número máximo de partículas
  let particles = [];

  canvas.width = W;
  canvas.height = H;

  function random(min, max) {
    return Math.random() * (max - min) + min;
  }

  function createParticle() {
    return {
      x: Math.random() * W,
      y: Math.random() * H,
      r: random(5, 15),
      d: random(10, 20), // Densidad para la velocidad
      color: rgba(${Math.floor(random(0, 256))}, ${Math.floor(random(0, 256))}, ${Math.floor(random(0, 256))}, 0.8),
      tilt: Math.floor(random(-10, 11)),
      tiltAngleIncrement: random(0.05, 0.1)
    };
  }

  function drawParticle(p) {
    ctx.beginPath();
    ctx.lineWidth = p.r / 2;
    ctx.strokeStyle = p.color;
    ctx.moveTo(p.x, p.y);
    ctx.lineTo(p.x + p.tilt + p.r / 2, p.y + p.tilt);
    ctx.stroke();
  }

  function updateParticle(p) {
    p.tiltAngle += p.tiltAngleIncrement;
    p.y += (Math.cos(p.d) + 1 + p.r / 2) / 2;
    p.x += Math.sin(p.tiltAngle) - 0.5;
    p.tilt = Math.sin(p.tiltAngle) * 12;

    if (p.x > W + 5 || p.x < -5 || p.y > H) {
      particles.splice(particles.indexOf(p), 1);
    }
  }

  function animateConfetti() {
    for (let i = 0; i < mp; i++) {
      particles.push(createParticle());
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        drawParticle(p);
        updateParticle(p);
      }
      requestAnimationFrame(draw);
    }
    draw();
  }

  // Iniciar la animación al cargar la página
  window.onload = animateConfetti;

  // Iniciar la animación cada 20 segundos
  setInterval(animateConfetti, 20000);

  window.addEventListener('resize', () => {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W;
    canvas.height = H;
  });

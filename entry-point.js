/* ========================================
   entry-point.js — Journey Entry Point Module
   DevOps AI by RainTech
   
   Full-screen neural network role selection experience.
   Concept A+C Hybrid: 3D Force Graph (desktop) + Card Grid (mobile/fallback).
   
   Feature-flagged via DEVOPS_AI_JOURNEY_ENTRY_POINT in personalization.js.
   This module is dynamically loaded only when the flag is enabled.
   
   Control plane: BD Zone → Customer Journey / CRM (FR-001)
   ======================================== */

(function() {
  'use strict';

  // ─── Zone Label Map ───
  var ZONE_LABELS = {
    'vc-suite': 'vC-Suite', 'analytics': 'Analytics', 'relationships': 'Relationships',
    'service-desk': 'Service Desk', 'endpoint-management': 'Endpoint Mgmt', 'endpoint-mgmt': 'Endpoint Mgmt',
    'network-ops': 'Network Ops', 'security-operations': 'Security Ops', 'security-ops': 'Security Ops',
    'grc-compliance': 'GRC & Compliance', 'projects': 'Projects', 'accounting': 'Accounting',
    'people': 'People', 'learning': 'Learning', 'organization': 'Organization',
    'legal': 'Legal', 'devops': 'DevOps'
  };

  var ZONE_LIST = [
    { id: 'vc-suite', label: 'vC-Suite' }, { id: 'analytics', label: 'Analytics' },
    { id: 'relationships', label: 'Relationships' }, { id: 'service-desk', label: 'Service Desk' },
    { id: 'endpoint-mgmt', label: 'Endpoint Mgmt' }, { id: 'network-ops', label: 'Network Ops' },
    { id: 'security-ops', label: 'Security Ops' }, { id: 'grc-compliance', label: 'GRC & Compliance' },
    { id: 'projects', label: 'Projects' }, { id: 'accounting', label: 'Accounting' },
    { id: 'people', label: 'People' }, { id: 'learning', label: 'Learning' },
    { id: 'organization', label: 'Organization' }, { id: 'legal', label: 'Legal' },
    { id: 'devops', label: 'DevOps' }
  ];

  // ─── Internal State ───
  var epState = {
    tier: null,
    selectedRole: null,
    hoveredRole: null,
    threeScene: null,
    config: null
  };

  // ─── Tier Detection ───
  function detectTier(mode) {
    if (mode === '3d') return 'full-3d';
    if (mode === 'cards') return 'card-grid';

    var isMobile = window.innerWidth < 768 || ('ontouchstart' in window && window.innerWidth < 1024);
    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (isMobile || prefersReducedMotion) return 'card-grid';

    try {
      var testCanvas = document.createElement('canvas');
      var gl = testCanvas.getContext('webgl2') || testCanvas.getContext('webgl');
      if (!gl) return 'card-grid';
      var debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
      if (debugInfo) {
        var renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL).toLowerCase();
        if (renderer.indexOf('swiftshader') >= 0 || renderer.indexOf('llvmpipe') >= 0) return 'card-grid';
      }
      return 'full-3d';
    } catch (e) {
      return 'card-grid';
    }
  }

  // ─── Build DOM ───
  function buildEntryPointDOM() {
    // Remove any existing entry point
    var existing = document.getElementById('devopsai-entry-point');
    if (existing) existing.remove();

    var container = document.createElement('div');
    container.id = 'devopsai-entry-point';
    container.className = 'ep-container';
    container.setAttribute('role', 'dialog');
    container.setAttribute('aria-label', 'Select your role in the DevOps AI network');

    container.innerHTML =
      '<canvas id="ep-network-canvas" class="ep-network-canvas" aria-label="Neural network visualization"></canvas>' +
      '<canvas id="ep-neural-bg" class="ep-neural-bg" aria-hidden="true"></canvas>' +
      '<header class="ep-header" id="ep-header">' +
        '<div class="ep-header__brand">' +
          '<svg class="ep-header__logo" viewBox="0 0 140 28" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="DevOps AI">' +
            '<text x="0" y="22" font-family="Plus Jakarta Sans, sans-serif" font-weight="800" font-size="22" fill="#F7F7FF">DevOps</text>' +
            '<text x="92" y="22" font-family="Plus Jakarta Sans, sans-serif" font-weight="800" font-size="22" fill="#8BDB02">AI</text>' +
          '</svg>' +
        '</div>' +
        '<button class="ep-header__skip" id="ep-skip-btn" aria-label="Skip role selection">Skip</button>' +
      '</header>' +
      '<div class="ep-prompt" id="ep-prompt">' +
        '<h2 class="ep-prompt__title">Where do you belong in this network?</h2>' +
        '<p class="ep-prompt__subtitle">Select your role to enter the DevOps AI platform. Every node is a human — every connection is intelligent.</p>' +
      '</div>' +
      '<div class="ep-detail" id="ep-detail" role="status" aria-live="polite">' +
        '<div class="ep-detail__inner">' +
          '<button class="ep-detail__back" id="ep-detail-back" aria-label="Back to all roles">' +
            '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>' +
            '<span>All Roles</span>' +
          '</button>' +
          '<div class="ep-detail__content">' +
            '<span class="ep-detail__badge" id="ep-detail-badge"></span>' +
            '<h3 class="ep-detail__title" id="ep-detail-title"></h3>' +
            '<p class="ep-detail__desc" id="ep-detail-desc"></p>' +
            '<div class="ep-detail__zones" id="ep-detail-zones"></div>' +
            '<button class="ep-detail__cta" id="ep-detail-cta">Enter as this role</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
      '<div class="ep-grid-container" id="ep-grid-container">' +
        '<div class="ep-grid" id="ep-grid" role="listbox" aria-label="Select your role"></div>' +
      '</div>' +
      '<div class="ep-confirm" id="ep-confirm" aria-hidden="true">' +
        '<div class="ep-confirm__card">' +
          '<div class="ep-confirm__ring"></div>' +
          '<h3 class="ep-confirm__title" id="ep-confirm-title"></h3>' +
          '<p class="ep-confirm__desc">Personalizing your DevOps AI experience...</p>' +
          '<div class="ep-confirm__loader"><div class="ep-confirm__bar"></div></div>' +
        '</div>' +
      '</div>' +
      (epState.config && epState.config.debug ? '<div class="ep-tier" id="ep-tier"></div>' : '');

    document.body.appendChild(container);
    return container;
  }

  // ─── Build Card Grid ───
  function buildCardGrid() {
    var config = epState.config;
    var grid = document.getElementById('ep-grid');
    if (!grid) return;

    var groupOrder = ['executive', 'operations', 'security', 'business', 'people'];

    groupOrder.forEach(function(groupId) {
      var group = config.groups[groupId];
      if (!group) return;
      var roles = config.roles.filter(function(r) { return r.group === groupId; });
      if (roles.length === 0) return;

      var section = document.createElement('div');
      section.className = 'ep-group';
      section.innerHTML =
        '<div class="ep-group__header">' +
          '<div class="ep-group__dot" style="background:' + group.color + '; box-shadow: 0 0 8px ' + group.color + '"></div>' +
          '<span class="ep-group__label">' + group.label + '</span>' +
        '</div>' +
        '<div class="ep-group__cards"></div>';

      var cardsEl = section.querySelector('.ep-group__cards');

      roles.forEach(function(role, i) {
        var card = document.createElement('button');
        card.className = 'ep-card';
        card.setAttribute('role', 'option');
        card.setAttribute('aria-selected', 'false');
        card.setAttribute('data-role-id', role.id);
        card.setAttribute('data-group', role.group);
        card.style.animationDelay = (i * 50) + 'ms';

        var zoneBadges = (role.zones || []).map(function(z) {
          return '<span class="ep-zone-badge">' + (ZONE_LABELS[z] || z) + '</span>';
        }).join('');

        card.innerHTML =
          '<span class="ep-card__name">' + role.label + '</span>' +
          '<span class="ep-card__desc">' + (role.desc || '') + '</span>' +
          '<div class="ep-card__zones">' + zoneBadges + '</div>';

        card.addEventListener('click', function() { selectRole(role); });
        cardsEl.appendChild(card);
      });

      grid.appendChild(section);
    });
  }

  // ─── Neural Canvas Background ───
  function initNeuralBackground() {
    var canvas = document.getElementById('ep-neural-bg');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');

    function resize() {
      var dpr = window.devicePixelRatio > 1 ? 2 : 1;
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
      canvas.style.width = window.innerWidth + 'px';
      canvas.style.height = window.innerHeight + 'px';
      if (dpr > 1) ctx.scale(2, 2);
    }
    resize();
    window.addEventListener('resize', resize);

    var w = window.innerWidth;
    var h = window.innerHeight;
    var nodeCount = Math.min(40, Math.floor((w * h) / 20000));
    var nodes = [];
    var colors = ['#17E4ED', '#20BAE7', '#8BDB02', '#C616EA', '#2272E0'];

    for (var i = 0; i < nodeCount; i++) {
      nodes.push({
        x: Math.random() * w, y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.3, vy: (Math.random() - 0.5) * 0.3,
        radius: Math.random() * 2 + 1, pulse: Math.random() * Math.PI * 2,
        color: colors[Math.floor(Math.random() * 5)]
      });
    }

    var connections = [];
    var maxDist = 200;
    for (var i2 = 0; i2 < nodes.length; i2++) {
      for (var j = i2 + 1; j < nodes.length; j++) {
        var dx = nodes[i2].x - nodes[j].x;
        var dy = nodes[i2].y - nodes[j].y;
        if (Math.sqrt(dx * dx + dy * dy) < maxDist) connections.push({ a: i2, b: j });
      }
    }

    var particles = connections.slice(0, 15).map(function(conn) {
      return { conn: conn, t: Math.random(), speed: 0.001 + Math.random() * 0.002 };
    });

    var animId;
    function animate() {
      var cw = window.innerWidth, ch = window.innerHeight;
      ctx.clearRect(0, 0, cw, ch);

      nodes.forEach(function(node) {
        node.x += node.vx; node.y += node.vy; node.pulse += 0.02;
        if (node.x < 0 || node.x > cw) node.vx *= -1;
        if (node.y < 0 || node.y > ch) node.vy *= -1;
      });

      connections.forEach(function(conn) {
        var a = nodes[conn.a], b = nodes[conn.b];
        var dx2 = a.x - b.x, dy2 = a.y - b.y;
        var dist = Math.sqrt(dx2 * dx2 + dy2 * dy2);
        var alpha = Math.max(0, 1 - dist / maxDist) * 0.08;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = 'rgba(23, 228, 237, ' + alpha + ')';
        ctx.lineWidth = 0.5; ctx.stroke();
      });

      particles.forEach(function(p) {
        p.t += p.speed; if (p.t > 1) p.t = 0;
        var a = nodes[p.conn.a], b = nodes[p.conn.b];
        var x = a.x + (b.x - a.x) * p.t, y = a.y + (b.y - a.y) * p.t;
        ctx.beginPath(); ctx.arc(x, y, 1.5, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(139, 219, 2, 0.6)'; ctx.fill();
      });

      nodes.forEach(function(node) {
        var glow = 0.3 + Math.sin(node.pulse) * 0.15;
        var r = parseInt(node.color.slice(1, 3), 16);
        var g = parseInt(node.color.slice(3, 5), 16);
        var bl = parseInt(node.color.slice(5, 7), 16);
        ctx.beginPath(); ctx.arc(node.x, node.y, node.radius + 4, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(' + r + ',' + g + ',' + bl + ',' + (glow * 0.15) + ')'; ctx.fill();
        ctx.beginPath(); ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(' + r + ',' + g + ',' + bl + ',' + (glow + 0.2) + ')'; ctx.fill();
      });

      animId = requestAnimationFrame(animate);
    }

    canvas.classList.add('is-active');
    animate();

    return function cleanup() { cancelAnimationFrame(animId); };
  }

  // ─── 3D Force Graph (Concept A) ───
  async function init3DGraph() {
    var canvas = document.getElementById('ep-network-canvas');
    var config = epState.config;
    if (!canvas || !config) return;

    try {
      var threeBase = 'https://cdn.jsdelivr.net/npm/three@0.170.0';
      var THREE = await import(threeBase + '/build/three.module.js');
      var OrbitControls = (await import(threeBase + '/examples/jsm/controls/OrbitControls.js')).OrbitControls;
      var EffectComposer = (await import(threeBase + '/examples/jsm/postprocessing/EffectComposer.js')).EffectComposer;
      var RenderPass = (await import(threeBase + '/examples/jsm/postprocessing/RenderPass.js')).RenderPass;
      var UnrealBloomPass = (await import(threeBase + '/examples/jsm/postprocessing/UnrealBloomPass.js')).UnrealBloomPass;

      function makeTextSprite(text, color) {
        var c2d = document.createElement('canvas');
        c2d.width = 512; c2d.height = 128;
        var ctx2d = c2d.getContext('2d');
        ctx2d.clearRect(0, 0, 512, 128);
        ctx2d.font = 'bold 36px Plus Jakarta Sans, sans-serif';
        ctx2d.textAlign = 'center';
        ctx2d.fillStyle = '#' + color.getHexString();
        ctx2d.globalAlpha = 0.85;
        ctx2d.fillText(text, 256, 72);
        var tex = new THREE.CanvasTexture(c2d);
        tex.needsUpdate = true;
        var mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false });
        var sprite = new THREE.Sprite(mat);
        sprite.scale.set(8, 2, 1);
        return sprite;
      }

      var scene = new THREE.Scene();
      scene.background = new THREE.Color(0x000E2E);

      var camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.set(0, 5, 55);

      var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: false });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.2;

      var composer = new EffectComposer(renderer);
      composer.addPass(new RenderPass(scene, camera));
      var bloomPass = new UnrealBloomPass(
        new THREE.Vector2(window.innerWidth, window.innerHeight), 0.8, 0.6, 0.4
      );
      composer.addPass(bloomPass);

      var controls = new OrbitControls(camera, canvas);
      controls.enableDamping = true; controls.dampingFactor = 0.05;
      controls.enablePan = false; controls.minDistance = 25; controls.maxDistance = 80;
      controls.autoRotate = true; controls.autoRotateSpeed = 0.3;

      var graphNodes = [];
      var linkObjects = [];
      var nodeObjects = new Map();

      // Hub
      var hubGeo = new THREE.SphereGeometry(2.5, 32, 32);
      var hubMat = new THREE.MeshBasicMaterial({ color: 0x8BDB02 });
      var hubMesh = new THREE.Mesh(hubGeo, hubMat);
      hubMesh.userData = { type: 'hub', id: 'devops-ai', label: 'DevOps AI' };
      scene.add(hubMesh);
      graphNodes.push({ id: 'hub', mesh: hubMesh, x: 0, y: 0, z: 0 });

      var hubLabel = makeTextSprite('DevOps AI', new THREE.Color(0x8BDB02));
      hubLabel.position.set(0, -3.5, 0); hubLabel.scale.set(10, 2.5, 1);
      scene.add(hubLabel);

      // Zone nodes
      var zoneRadius = 15;
      ZONE_LIST.forEach(function(zone, i) {
        var angle = (i / ZONE_LIST.length) * Math.PI * 2;
        var elev = (Math.random() - 0.5) * 6;
        var x = Math.cos(angle) * zoneRadius, y = elev, z = Math.sin(angle) * zoneRadius;

        var geo = new THREE.SphereGeometry(0.6, 16, 16);
        var mat = new THREE.MeshBasicMaterial({ color: 0x17E4ED, transparent: true, opacity: 0.5 });
        var mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(x, y, z);
        mesh.userData = { type: 'zone', id: zone.id, label: zone.label };
        scene.add(mesh);
        nodeObjects.set(zone.id, mesh);
        graphNodes.push({ id: zone.id, mesh: mesh, x: x, y: y, z: z });

        addLink(hubMesh.position, mesh.position, 0x17E4ED, 0.15);
      });

      // Role nodes
      var roleRadius = 28;
      var groupOffsets = { executive: 0, operations: 1, security: 2, business: 3, people: 4 };
      var groupCounts = {};
      config.roles.forEach(function(r) { groupCounts[r.group] = (groupCounts[r.group] || 0) + 1; });
      var groupRunning = {};

      config.roles.forEach(function(role) {
        var gIdx = groupOffsets[role.group];
        if (!groupRunning[role.group]) groupRunning[role.group] = 0;
        var withinGroup = groupRunning[role.group]++;

        var groupAngleStart = (gIdx / 5) * Math.PI * 2;
        var groupAngleSpan = (1 / 5) * Math.PI * 2;
        var angleInGroup = groupAngleStart + (withinGroup / groupCounts[role.group]) * groupAngleSpan + groupAngleSpan * 0.1;

        var elev = (Math.random() - 0.5) * 8;
        var x = Math.cos(angleInGroup) * roleRadius, y = elev, z = Math.sin(angleInGroup) * roleRadius;

        var groupColor = new THREE.Color(config.groups[role.group].color);
        var geo = new THREE.SphereGeometry(1.0, 24, 24);
        var mat = new THREE.MeshBasicMaterial({ color: groupColor, transparent: true, opacity: 0.85 });
        var mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(x, y, z);
        mesh.userData = { type: 'role', id: role.id, label: role.label, desc: role.desc, group: role.group, zones: role.zones };
        scene.add(mesh);
        nodeObjects.set(role.id, mesh);
        graphNodes.push({ id: role.id, mesh: mesh, x: x, y: y, z: z, role: role });

        var labelSprite = makeTextSprite(role.label, groupColor);
        labelSprite.position.set(x, y - 2, z);
        scene.add(labelSprite);
        mesh.userData.labelSprite = labelSprite;

        // Normalize zone IDs for linking
        var normalizedZones = (role.zones || []).map(function(zId) {
          // Map long names to short ones used in ZONE_LIST
          if (zId === 'security-operations') return 'security-ops';
          if (zId === 'endpoint-management') return 'endpoint-mgmt';
          return zId;
        });

        normalizedZones.forEach(function(zoneId) {
          var zoneMesh = nodeObjects.get(zoneId);
          if (zoneMesh) {
            addLink(mesh.position, zoneMesh.position, parseInt(config.groups[role.group].color.slice(1), 16), 0.12);
          }
        });
      });

      function addLink(posA, posB, color, opacity) {
        var points = [posA.clone(), posB.clone()];
        var geo = new THREE.BufferGeometry().setFromPoints(points);
        var mat = new THREE.LineBasicMaterial({ color: color, transparent: true, opacity: opacity });
        var line = new THREE.Line(geo, mat);
        scene.add(line);
        linkObjects.push({ line: line, posA: posA, posB: posB, baseOpacity: opacity, mat: mat });
      }

      // Particles
      var particleCount = Math.min(linkObjects.length, 40);
      var particleGeo = new THREE.SphereGeometry(0.15, 8, 8);
      var particleMat = new THREE.MeshBasicMaterial({ color: 0x8BDB02, transparent: true, opacity: 0.8 });
      var particles = [];

      for (var p = 0; p < particleCount; p++) {
        var linkIdx = p % linkObjects.length;
        var link = linkObjects[linkIdx];
        var pmesh = new THREE.Mesh(particleGeo, particleMat.clone());
        pmesh.position.copy(link.posA);
        scene.add(pmesh);
        particles.push({ mesh: pmesh, link: link, t: Math.random(), speed: 0.002 + Math.random() * 0.003 });
      }

      // Aurora background
      var auroraGeo = new THREE.PlaneGeometry(200, 200);
      var auroraMat = new THREE.ShaderMaterial({
        uniforms: {
          uTime: { value: 0 },
          uColor1: { value: new THREE.Color(0x001647) },
          uColor2: { value: new THREE.Color(0x05108E) },
          uColor3: { value: new THREE.Color(0x0a0a2e) }
        },
        vertexShader: 'varying vec2 vUv; void main() { vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
        fragmentShader: 'uniform float uTime; uniform vec3 uColor1; uniform vec3 uColor2; uniform vec3 uColor3; varying vec2 vUv; void main() { float t = sin(uTime * 0.3 + vUv.x * 3.0) * 0.5 + 0.5; float t2 = cos(uTime * 0.2 + vUv.y * 2.0) * 0.5 + 0.5; vec3 color = mix(mix(uColor1, uColor2, t), uColor3, t2); gl_FragColor = vec4(color, 1.0); }',
        side: THREE.DoubleSide
      });
      var auroraMesh = new THREE.Mesh(auroraGeo, auroraMat);
      auroraMesh.position.z = -50;
      scene.add(auroraMesh);

      // Hover interaction
      var raycaster = new THREE.Raycaster();
      var mouse = new THREE.Vector2();
      var hoveredMesh = null;
      var previewCard = createPreviewCard();

      canvas.addEventListener('mousemove', function(e) {
        mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
        raycaster.setFromCamera(mouse, camera);
        var roleMeshes = graphNodes.filter(function(n) { return n.role; }).map(function(n) { return n.mesh; });
        var intersects = raycaster.intersectObjects(roleMeshes);

        if (intersects.length > 0) {
          var m = intersects[0].object;
          if (hoveredMesh !== m) {
            if (hoveredMesh) unhoverNode(hoveredMesh);
            hoveredMesh = m;
            hoverNode(m, e.clientX, e.clientY);
          } else {
            updatePreviewPos(e.clientX, e.clientY);
          }
          canvas.style.cursor = 'pointer';
        } else {
          if (hoveredMesh) { unhoverNode(hoveredMesh); hoveredMesh = null; }
          canvas.style.cursor = 'default';
          hidePreview();
        }
      });

      canvas.addEventListener('click', function() {
        if (hoveredMesh && hoveredMesh.userData.type === 'role') {
          var role = config.roles.find(function(r) { return r.id === hoveredMesh.userData.id; });
          if (role) selectRole(role);
        }
      });

      function hoverNode(mesh, mx, my) {
        mesh.scale.setScalar(1.3);
        linkObjects.forEach(function(lo) { lo.mat.opacity = 0.03; });
        var role = config.roles.find(function(r) { return r.id === mesh.userData.id; });
        if (role) {
          (role.zones || []).forEach(function(zId) {
            var nzId = zId === 'security-operations' ? 'security-ops' : zId === 'endpoint-management' ? 'endpoint-mgmt' : zId;
            var zm = nodeObjects.get(nzId);
            if (zm) { zm.scale.setScalar(1.1); zm.material.opacity = 1.0; }
          });
        }
        showPreview(mesh.userData, mx, my);
      }

      function unhoverNode(mesh) {
        mesh.scale.setScalar(1.0);
        linkObjects.forEach(function(lo) { lo.mat.opacity = lo.baseOpacity; });
        ZONE_LIST.forEach(function(z) {
          var zm = nodeObjects.get(z.id);
          if (zm) { zm.scale.setScalar(1.0); zm.material.opacity = 0.6; }
        });
      }

      function createPreviewCard() {
        var card = document.createElement('div');
        card.className = 'ep-preview';
        card.innerHTML = '<div class="ep-preview__name"></div><div class="ep-preview__desc"></div><div class="ep-preview__zones"></div>';
        document.body.appendChild(card);
        return card;
      }

      function showPreview(data, mx, my) {
        previewCard.querySelector('.ep-preview__name').textContent = data.label;
        previewCard.querySelector('.ep-preview__desc').textContent = data.desc || '';
        if (data.zones) {
          previewCard.querySelector('.ep-preview__zones').innerHTML =
            data.zones.map(function(z) { return '<span class="ep-zone-badge">' + (ZONE_LABELS[z] || z) + '</span>'; }).join('');
        }
        updatePreviewPos(mx, my);
        previewCard.classList.add('is-visible');
      }

      function updatePreviewPos(mx, my) {
        var x = mx + 20, y = my - 10;
        if (x + 280 > window.innerWidth) x = mx - 300;
        if (y + 120 > window.innerHeight) y = window.innerHeight - 130;
        if (y < 10) y = 10;
        previewCard.style.left = x + 'px';
        previewCard.style.top = y + 'px';
      }

      function hidePreview() { previewCard.classList.remove('is-visible'); }

      // Resize
      function onResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
        composer.setSize(window.innerWidth, window.innerHeight);
      }
      window.addEventListener('resize', onResize);

      // Animate
      var clock = new THREE.Clock();
      var animRunning = true;

      function animate() {
        if (!animRunning) return;
        requestAnimationFrame(animate);
        var elapsed = clock.getElapsedTime();
        auroraMat.uniforms.uTime.value = elapsed;
        hubMesh.scale.setScalar(1.0 + Math.sin(elapsed * 1.5) * 0.05);
        particles.forEach(function(pt) {
          pt.t += pt.speed; if (pt.t > 1) pt.t = 0;
          pt.mesh.position.lerpVectors(pt.link.posA, pt.link.posB, pt.t);
          pt.mesh.material.opacity = Math.sin(pt.t * Math.PI) * 0.8;
        });
        graphNodes.forEach(function(node) {
          if (node.role && node.mesh !== hoveredMesh) {
            node.mesh.scale.setScalar(1.0 + Math.sin(elapsed * 0.8 + node.x) * 0.03);
          }
        });
        controls.update();
        composer.render();
      }

      // Universe Awakening sequence
      canvas.classList.add('is-active');
      graphNodes.forEach(function(node, i) {
        node.mesh.scale.setScalar(0.001);
        var delay = node.id === 'hub' ? 600 : node.mesh.userData.type === 'zone' ? 900 + i * 80 : 1500 + i * 60;
        setTimeout(function() { animateSpring(node.mesh.scale, { x: 1, y: 1, z: 1 }, 400); }, delay);
      });
      linkObjects.forEach(function(lo, i) {
        lo.mat.opacity = 0;
        setTimeout(function() { lo.mat.opacity = lo.baseOpacity; }, 1200 + i * 20);
      });
      particles.forEach(function(pt, i) {
        pt.mesh.visible = false;
        setTimeout(function() { pt.mesh.visible = true; }, 2000 + i * 50);
      });

      animate();
      epState.threeScene = { scene: scene, camera: camera, renderer: renderer, composer: composer, controls: controls };

    } catch (err) {
      console.warn('[DevOps AI Entry Point] 3D init failed, falling back to card grid:', err);
      epState.tier = 'card-grid';
      canvas.style.display = 'none';
      initCardGridMode();
    }
  }

  function animateSpring(obj, target, duration) {
    var start = { x: obj.x, y: obj.y, z: obj.z };
    var startTime = performance.now();
    function step(now) {
      var t = Math.min((now - startTime) / duration, 1);
      var spring = 1 - Math.pow(1 - t, 3) * Math.cos(t * Math.PI * 0.5);
      obj.x = start.x + (target.x - start.x) * spring;
      obj.y = start.y + (target.y - start.y) * spring;
      obj.z = start.z + (target.z - start.z) * spring;
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // ─── Role Selection ───
  function selectRole(role) {
    epState.selectedRole = role;
    var config = epState.config;

    var panel = document.getElementById('ep-detail');
    var badge = document.getElementById('ep-detail-badge');
    var title = document.getElementById('ep-detail-title');
    var desc = document.getElementById('ep-detail-desc');
    var zonesEl = document.getElementById('ep-detail-zones');

    var group = config.groups[role.group] || { label: '', color: '#8BDB02' };
    badge.textContent = group.label;
    badge.style.background = group.color + '20';
    badge.style.color = group.color;
    title.textContent = role.label;
    desc.textContent = role.desc || '';

    zonesEl.innerHTML =
      '<span class="ep-detail__zones-label">Connected AI Zones</span>' +
      (role.zones || []).map(function(z) {
        return '<div class="ep-zone-item"><div class="ep-zone-dot"></div><span class="ep-zone-name">' + (ZONE_LABELS[z] || z) + '</span></div>';
      }).join('');

    panel.classList.add('is-open');

    document.querySelectorAll('.ep-card').forEach(function(card) {
      card.setAttribute('aria-selected', card.dataset.roleId === role.id ? 'true' : 'false');
    });
  }

  function deselectRole() {
    epState.selectedRole = null;
    document.getElementById('ep-detail').classList.remove('is-open');
    document.querySelectorAll('.ep-card').forEach(function(card) {
      card.setAttribute('aria-selected', 'false');
    });
  }

  function confirmRole() {
    if (!epState.selectedRole || !epState.config) return;

    var overlay = document.getElementById('ep-confirm');
    var title = document.getElementById('ep-confirm-title');
    title.textContent = 'Welcome, ' + epState.selectedRole.label;
    overlay.classList.add('is-active');
    overlay.setAttribute('aria-hidden', 'false');

    // Trigger the callback to personalization.js
    setTimeout(function() {
      if (epState.config.onRoleSelected) {
        epState.config.onRoleSelected(epState.selectedRole.id);
      }
    }, 2200);
  }

  // ─── Mode Init ───
  function initCardGridMode() {
    initNeuralBackground();
    var gridContainer = document.getElementById('ep-grid-container');
    if (gridContainer) gridContainer.classList.remove('is-hidden');

    setTimeout(function() {
      var h = document.getElementById('ep-header'); if (h) h.classList.add('is-visible');
    }, 300);
    setTimeout(function() {
      var p = document.getElementById('ep-prompt'); if (p) p.classList.add('is-visible');
    }, 600);
    setTimeout(function() {
      var g = document.getElementById('ep-grid-container'); if (g) g.classList.add('is-visible');
    }, 800);
  }

  function init3DMode() {
    var container = document.getElementById('devopsai-entry-point');
    if (container) container.classList.add('mode-3d');

    var gridContainer = document.getElementById('ep-grid-container');
    if (gridContainer) gridContainer.classList.add('is-hidden');

    setTimeout(function() {
      var h = document.getElementById('ep-header'); if (h) h.classList.add('is-visible');
    }, 300);
    setTimeout(function() {
      var p = document.getElementById('ep-prompt'); if (p) p.classList.add('is-visible');
    }, 2500);

    init3DGraph();
  }

  // ─── Main Init ───
  function initEntryPoint(config) {
    epState.config = config;
    epState.selectedRole = null;
    epState.tier = detectTier(config.mode);

    buildEntryPointDOM();
    buildCardGrid();

    if (config.debug) {
      var tierEl = document.getElementById('ep-tier');
      if (tierEl) tierEl.textContent = 'Tier: ' + epState.tier;
    }

    // Wire events
    var backBtn = document.getElementById('ep-detail-back');
    if (backBtn) backBtn.addEventListener('click', deselectRole);

    var ctaBtn = document.getElementById('ep-detail-cta');
    if (ctaBtn) ctaBtn.addEventListener('click', confirmRole);

    var skipBtn = document.getElementById('ep-skip-btn');
    if (skipBtn) {
      skipBtn.addEventListener('click', function() {
        var container = document.getElementById('devopsai-entry-point');
        if (container) {
          container.classList.add('is-hidden');
          setTimeout(function() { container.remove(); }, 600);
        }
      });
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        if (epState.selectedRole) deselectRole();
      }
    });

    // Launch appropriate tier
    if (epState.tier === 'full-3d') {
      init3DMode();
    } else {
      initCardGridMode();
    }
  }

  // ─── Bootstrap ───
  // Check if config is already available (personalization.js loaded first)
  if (window.__DEVOPS_AI_ENTRY_POINT__) {
    initEntryPoint(window.__DEVOPS_AI_ENTRY_POINT__);
  }

  // Expose init function for dynamic loading
  window.__devopsAIEntryPointInit = initEntryPoint;

})();

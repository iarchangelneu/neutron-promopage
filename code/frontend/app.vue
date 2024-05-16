<template>
  <div>
    <TheHeader />
    <div class="main-wrapper" style="z-index: 2;">
      <NuxtPage />
    </div>
    <div class="footer-wrapper">
      <TheFooter ref="footer" />
    </div>
  </div>
</template>

<template>
  <ion-app>
    <ion-split-pane content-id="main-content">
      <ion-menu content-id="main-content" type="overlay">
        <ion-content>
          <ion-img src="/logo.png"></ion-img>
          <ion-menu-toggle :auto-hide="false" v-for="(p, i) in appPages" :key="i">
            <ion-item @click="selectedIndex = i" router-direction="root" :router-link="p.url" lines="none" :detail="false"
              class="hydrated" :class="{ selected: selectedIndex === i }">
              <ion-label>{{ p.title }}</ion-label>
            </ion-item>
          </ion-menu-toggle>
          <ion-item id="salir">
            <ion-label>Salir</ion-label>
          </ion-item>
        </ion-content>
      </ion-menu>
      <ion-header id="celular">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="light"></ion-menu-button>
          </ion-buttons>
          <Ion-img src="/logo.png"></Ion-img>
        </ion-toolbar>
      </ion-header>
      <ion-router-outlet id="main-content"></ion-router-outlet>
    </ion-split-pane>
  </ion-app>
</template>

<script setup lang="ts">
import {
  IonApp,
  IonContent,
  IonItem,
  IonLabel,
  IonMenu,
  IonMenuToggle,
  IonImg,
  IonRouterOutlet,
  IonSplitPane,
  IonHeader,
  IonToolbar,
  IonButtons,
  IonMenuButton
} from '@ionic/vue';
import { ref } from 'vue';

const selectedIndex = ref(0);
const appPages = [
  {
    title: 'Pozos',
    url: '/admin/lista-pozos',
  },
  {
    title: 'Control Remoto',
    url: '/admin/control-pozo',
  },
  {
    title: 'Usuarios',
    url: '/admin/lista-usuarios',
  },
  {
    title: 'Reportes',
    url: '/admin/generar-reporte',
  }
];
</script>

<style scoped>
ion-menu ion-content {
  --background: #D4D4D4;
}

ion-toolbar {
  --background: #D4D4D4;
}

ion-toolbar ion-img {
  width: 50%;
  float: right;
  margin-right: 10px;
}

ion-img {
  width: 0%;
  height: 10%;
}

ion-item {
  --background: transparent;
  margin-top: 30px;
  text-align: center;
  color: #000;
  --border-color: transparent;
}

#salir {
  margin-top: 55%;
}

ion-menu ion-item.selected {
  --background: #E5007E;
}

ion-menu.md ion-item ion-label {
  font-weight: 700;
}

@media screen and (min-width: 768px) {
  #celular {
    display: none;
  }

  ion-menu{
    width: 300px;
  }

  ion-img {
    width: 80%;
    margin: 10px auto;
    display: block;
  }
}
</style>

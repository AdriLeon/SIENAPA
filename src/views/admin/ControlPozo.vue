<template>
    <ion-split-pane when="md" contentId="main">
        <ion-menu contentId="main">
            <ion-content>
                <ion-img src="/caamt.gob.mx_.png"></ion-img>
                <ion-label class="ion-label-first"><a href="/admin/lista-pozos">Pozos</a></ion-label>
                <ion-label class="ion-label-selected"><a href="/admin/control-pozo">Control Remoto</a></ion-label>
                <ion-label class="ion-label"><a href="/admin/lista-usuarios">Usuarios</a></ion-label>
                <ion-label class="ion-label"><a href="/admin/generar-reporte">Reportes</a></ion-label>
                <ion-label class="ion-label-last"><a href="#">Salir</a></ion-label>
            </ion-content>
        </ion-menu>
        <div class="ion-page" id="main">
            <ion-header id="celular">
                <ion-toolbar>
                    <ion-buttons slot="start">
                        <ion-menu-button color="light"></ion-menu-button>
                        <img src="/caamt.gob.mx_.png" class="img-logo">
                    </ion-buttons>
                </ion-toolbar>
            </ion-header>
            <ion-content class="ion-padding">
                <ion-text>
                    <h1>Control Pozo</h1>
                </ion-text>
                <div class="container">
                    <select class="select">
                        <option value="selecciona">Selecciona un Pozo</option>
                        <option value="pozo1">Pozo 1</option>
                        <option value="pozo2">Pozo 2</option>
                        <option value="pozo3">Pozo 3</option>
                    </select>
                </div>
                <ion-grid fixed="xs">
                    <div id="base">
                        <ion-row>
                            <ion-col size="6" size-xs="12" size-md="6">
                                <div class="">
                                    <div class="row">
                                        <h5>Horario Programado</h5>
                                        <p id="horario">08:00 - 20:00</p>
                                        <p id="cambiar-horario"><a href="#">Cambiar horario</a></p>
                                    </div>
                                </div>
                            </ion-col>
                            <ion-col size="6" size-xs="12" size-md="6">
                                <div class="row">
                                    <h5>Encender/Apagar</h5>
                                    <ion-toggle labelPlacement="fixed" mode="ios"></ion-toggle>
                                </div>
                            </ion-col>
                        </ion-row>
                    </div>
                </ion-grid>
            </ion-content>
        </div>
    </ion-split-pane>
</template>
<script setup lang ="ts">
import {
    IonButtons,
    IonMenuButton,
    IonSplitPane,
    IonMenu,
    IonContent,
    IonHeader,
    IonToolbar,
    IonLabel,
    IonText,
    IonImg,
    IonToggle
} from '@ionic/vue';
</script>

<style>

ion-menu ion-content {
    --background: #D4D4D4;
}

ion-content {
    background-color: #D4D4D4;
}

.img-logo {
    margin-left: auto;
    max-width: 45%;
    float: right;
    display: block;
}

ion-img {
    margin: 0% auto;
    max-width: 75%;
    display: block;
}

ion-toolbar {
    --background: #D4D4D4;
}

ion-menu .ion-label a,
.ion-label-selected a,
.ion-label-first a,
.ion-label-last a {
    font-size: 20px;
    font-weight: bold;
    text-decoration: none;
    color: black;
}

.ion-label,
.ion-label-selected,
.ion-label-first,
.ion-label-last {
    text-align: center;
    display: block;
    background-color: #D4D4D4;
    padding: 20px;
    margin-top: 20px;
}

.ion-label-selected {
    background-color: #E5007E;
}

.ion-label-first {
    margin-top: 50px;
}

.ion-label-last {
    margin-top: 60%;
}

ion-text {
    --color: black;
    text-align: center;
}

#base {
    background: #D4D4D4;
    position: absolute;
    margin-top: 200px;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    height: auto;
    border-radius: 10px;
}

.container {
    display: flex;
    justify-content: center;
    margin-top: 30px;
    margin-bottom: 60px;
}

.select {
    border-radius: 10px;
    border: none;
    background-color: #D4D4D4;
    color: black;
    border: none;
    width: 200px;
    height: 40px;
    font-weight: bold;
    font-size: 16px;
}

.select option {
    font-weight: bold;
    font-size: 16px;
}

.row {
    flex: 1;
    align-self: center;
    text-align: center;
    color: #000;
    padding: 0.5em;
}

.row * {
    margin-bottom: 50px;
    font-size: 20px;
    color: #000;
}

ion-toggle {
    --handle-width: 35px;
    --handle-height: 35px;
    --track-background: #fff;
    --track-background-checked: #fff;
    --handle-background: #fa1900;
    --handle-background-checked: #99ff00;
    border-radius: 50px;
}

ion-toggle::part(track),
ion-toggle.toggle-checked::part(track) {
    height: 45px;
    width: 80px;
    border-radius: 50px;
    background: #fff;
    overflow: visible;
}

@media (min-width: 768px) {
    ion-content {
        background-image: url("../../../public/fondo.jpg");
        background-size: cover;
        background-position: center;
    }

    #celular {
        display: none;
    }

    .img-logo{
        width: 70px;
    }


    .ion-label-first {
        margin-top: 40px;
    }

    .ion-label-last {
        margin-top: 50%;
    }

}
</style>
<template>
    <ion-split-pane when="md" contentId="main">
        <ion-menu contentId="main">
            <ion-content>
                <ion-img src="/caamt.gob.mx_.png"></ion-img>
                <ion-label class="ion-label-first"><a href="/informatica/agregar-usuario">Agregar Usuarios</a></ion-label>
                <ion-label class="ion-label-selected"><a href="/informatica/modificar-usuario">Modificar
                        Usuarios</a></ion-label>
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
                    <h1>Modificar Usuarios</h1>
                </ion-text>
                <ion-grid fixed>
                    <ion-row>
                        <ion-col size="6" size-xs="12" size-md="6">
                            <ion-text>Correo Electronico</ion-text>
                            <br><br>
                            <ion-item>
                                <ion-select fill="solid" aria-label="Fruit" interface="popover" justify="start"
                                    placeholder="Correo Electronico">
                                    <ion-select-option value="mail1">mail1@email.com</ion-select-option>
                                </ion-select>
                            </ion-item>
                        </ion-col>
                        <ion-col size="6" size-xs="12" size-md="6">
                            <ion-text>Contraseña</ion-text>
                            <br><br>
                            <ion-item>
                                <ion-input type="password" placeholder="********"></ion-input>
                            </ion-item>
                        </ion-col>
                    </ion-row>
                    <ion-row>
                        <ion-col size="6" size-xs="12" size-md="6">
                            <ion-text>Nivel</ion-text>
                            <br><br>
                            <ion-row>
                                <ion-button>Administrador</ion-button>
                                <ion-button>Operador</ion-button>
                            </ion-row>
                        </ion-col>
                    </ion-row>
                    <ion-row id="button-mod">
                        <ion-button type="submit">Modificar Usuario</ion-button>
                    </ion-row>
                    <ion-row id="button-elim">
                        <ion-button type="submit" color="danger">Eliminar Usuario</ion-button>
                    </ion-row>
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
    IonGrid,
    IonRow,
    IonCol,
    IonSelect,
    IonSelectOption,
    IonButton,
    IonItem
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
    max-width: 75%;
    display: relative;
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

ion-grid {
    position: absolute;
    margin-top: 250px;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    height: auto;
    border-radius: 10px;
    text-align: center;
}

ion-select {
    --background: #ffffff;
    --placeholder-color: #000;
    justify-content: center;
    color: #000;
}

ion-select,
ion-item {
    --background: #D4D4D4;
    --placeholder-color: #000;
    --color: #000;
}

ion-col ion-row {
    width: 300px;
    justify-content: space-evenly;
}

ion-button {
    --color: #000;
    --background: #ffffff;
    --background-activated-opacity: 100;
    --background-activated: #E5007E;
}

#button-mod {
    justify-content: center;
    margin-top: 30px;
}

#button-elim {
    justify-content: center;
    margin-top: 20px;
}

@media (min-width: 768px) {
    ion-content {
        background-image: url("/fondo.jpg");
        background-size: cover;
        background-position: center;
    }

    #celular {
        display: none;
    }

    .img-logo {
        width: 70px;
    }


    .ion-label-first {
        margin-top: 40px;
    }

    .ion-label-last {
        margin-top: 50%;
    }

    ion-grid {
        position: absolute;
        margin-top: 200px;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        height: auto;
        border-radius: 10px;
    }

    ion-col ion-row {
        width: 400px;
        justify-content: space-evenly;
    }

    ion-item {
        margin-left: 15%;
        width: 300px;
    }

    #button-elim {
        justify-content: end;
        margin-top: 20px;
    }

}
</style>
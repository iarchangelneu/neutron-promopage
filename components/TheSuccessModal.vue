<template>
    <div class="success" @click="close_success">
        <div class="success__body" @click.stop>
            <div class="text-right">
                <button @click="close_success">
                    <img src="@/assets/img/close_modal.svg" alt="Закрыть">
                </button>
            </div>

            <div class="success__body--text">
                <span>Заявка успешно отправлена!</span>
                <small>Мы свяжемся с вами для дальнейшего сотрудничества</small>
                <button @click="close_success">Спасибо!</button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        close_success() {
            this.$emit('close-success');
        },
    }
}
</script>
<style lang="scss" scoped>
.success {
    background: rgba(255, 255, 255, 0.4);
    position: fixed;
    height: 100%;
    width: 100%;
    left: 0;
    top: 0;

    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 25;

    padding: 0 20px;


    &__body {
        border-radius: 30px;
        background: #0d0d0d;

        width: 1270px;
        height: 671px;

        padding: 50px;

        transition: all .3s ease;
        transform: scale(0);
        animation: scaleOut 0.5s ease forwards;

        @media (max-width: 1024px) {
            width: 355px;
            height: auto;
            padding: 15px;
        }

        &--text {
            margin-top: 75px;
            display: flex;
            flex-direction: column;
            gap: 50px;

            justify-content: center;
            align-items: center;

            @media (max-width: 1024px) {
                margin-top: 0;
                gap: 15px;
            }

            span {
                font-weight: 600;
                font-size: 64px;
                line-height: 130%;
                font-family: var(--int);
                color: #fff;
                text-align: center;

                @media (max-width: 1024px) {
                    font-size: 24px;

                }

            }

            small {
                font-weight: 400;
                font-size: 24px;
                line-height: 130%;
                font-family: var(--int);
                color: #fff;
                text-align: center;

                @media (max-width: 1024px) {
                    font-size: 16px;
                    max-width: 261px;
                }

            }

            button {
                padding: 15px 198px;
                border: 0;
                border-radius: 39px;
                background: #aa7cff;

                font-weight: 500;
                font-size: 24px;
                line-height: 130%;
                font-family: var(--ibm);
                color: #fff;

                transition: all .3s ease;

                @media (max-width: 1024px) {
                    padding: 7px 0 10px 0;
                    width: 100%;
                    margin-top: 30px;
                }


                &:hover {
                    background: #8b67cd;
                }

                &:active {
                    background: #aa7cff;
                }
            }
        }

        .text-right {
            button {
                border: 0;
                background: transparent;
                padding: 0;

                img {
                    @media (max-width: 1024px) {
                        width: 13px;
                    }
                }
            }
        }
    }

    @keyframes scaleOut {
        to {
            transform: scale(1);
        }
    }
}
</style>
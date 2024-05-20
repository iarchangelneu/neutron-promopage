<template>
    <footer>
        <div class="footer">
            <div class="footer__copyright">
                <img src="@/assets/img/neutron_logo.svg" alt="Логотип компании">
                <span>© 2024 ALL RIGHTS RESERVED.<br>ТОО “НЕЙТРОН”</span>
            </div>

            <div class="footer__socials">
                <a href="tel:+7 700 557-57-09">+7 700 557-57-09</a>

                <div>

                    <a href="https://wa.me/+77005575709" target="_blank">
                        <img src="@/assets/img/wa_social.svg" alt="Наш WhatsApp">
                    </a>
                    <a href="https://t.me/IlyaSushin" target="_blank">
                        <img src="@/assets/img/tg_social.svg" alt="Наш Telegram">
                    </a>
                    <a href="https://www.behance.net/neutronagency" target="_blank">
                        <img src="@/assets/img/beh_social.svg" alt="Наш Behance">
                    </a>
                </div>
            </div>

            <div class="footer__mobile">
                <a href="tel:+7 700 557-57-09">+7 700 557-57-09</a>

                <div>
                    <a href="https://wa.me/+77005575709" target="_blank">
                        <img src="@/assets/img/wa_social.svg" alt="Наш WhatsApp">
                    </a>
                    <a href="https://t.me/IlyaSushin" target="_blank">
                        <img src="@/assets/img/tg_social.svg" alt="Наш Telegram">
                    </a>
                    <a href="https://www.behance.net/neutronagency" target="_blank">
                        <img src="@/assets/img/beh_social.svg" alt="Наш Behance">
                    </a>
                    <div>
                        <img src="@/assets/img/neutron_logo.svg" alt="Логотип компании">
                        <span>© 2024 ALL RIGHTS RESERVED.<br> ТОО “НЕЙТРОН”</span>
                    </div>
                </div>
            </div>

            <img class="neutron_footer" src="@/assets/img/neutron_footer.svg" alt="Нейтрон - Диджитал студия
с современным взглядом на IT">
        </div>
    </footer>
</template>
<style lang="scss" scoped>
footer {
    padding: 0 60px;
    min-height: 546px;
    position: fixed;
    bottom: 0px;
    left: 0px;
    z-index: 1;
    width: 100%;
    transition: all .3s ease;

    @media (max-width: 1500px) {
        min-height: 480px;
        padding: 0 40px;
    }

    @media (max-width: 1400px) {
        min-height: 430px;
        padding: 0 40px;
    }

    @media (max-width: 1300px) {
        min-height: 330px;
        padding: 0 40px;
    }

    @media (max-width: 1024px) {
        min-height: 330px;
        padding: 0 10px;
    }

    @media (max-width: 768px) {
        min-height: 250px;
    }

    @media (max-width: 500px) {
        min-height: 130px;
    }

    .neutron_footer {
        position: absolute;
        left: 0;
        max-width: 100%;
        width: 100%;
    }

    .footer {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;

        .footer__mobile {
            margin-top: -130px;
            flex-direction: column;
            gap: 20px;
            display: none;
            z-index: 5;

            @media (max-width: 500px) {
                display: flex;
            }

            a {
                font-weight: 400;
                font-size: 20px;
                line-height: 130%;
                font-family: var(--ibm);
                color: #fff;
                text-decoration: none;
            }

            div {
                display: flex;
                align-items: flex-start;
                gap: 15px;

                img {
                    width: 40px;
                }

                div {
                    display: flex;
                    gap: 10px;
                    align-items: center;

                    span {
                        font-weight: 400;
                        font-size: 9px;
                        line-height: 130%;
                        font-family: var(--ibm);
                        color: #fff;
                    }
                }
            }
        }



        &__socials {
            display: flex;
            align-items: flex-end;
            flex-direction: column;
            gap: 30px;
            z-index: 5;


            @media (max-width: 1500px) {
                margin-top: -50px;
            }

            @media (max-width: 1024px) {
                margin-top: -100px;
            }

            @media (max-width: 768px) {
                margin-top: -180px;
            }

            @media (max-width: 500px) {
                display: none;
            }

            a {
                font-weight: 400;
                font-size: 45px;
                line-height: 130%;
                text-align: center;
                color: #fff;
                text-decoration: none;
            }

            div {
                display: flex;
                gap: 30px;
            }
        }

        &__copyright {
            display: flex;
            align-items: flex-start;
            flex-direction: column;
            gap: 56px;
            z-index: 5;

            @media (max-width: 1500px) {
                margin-top: -50px;
            }

            @media (max-width: 1024px) {
                margin-top: -100px;
            }

            @media (max-width: 768px) {
                margin-top: -180px;
            }

            @media (max-width: 500px) {
                display: none;
            }

            span {
                font-weight: 400;
                font-size: 14px;
                line-height: 130%;
                font-family: var(--int);
                color: #fff;
            }
        }
    }
}
</style>
<template>
    <header class="pc">
        <NuxtLink to="/" class="header__logo" :class="{ scrolled: isScrolled }">
            <img src="@/assets/img/neutron_logo.svg" alt="Логотип компании">
            <span>нейтрон</span>
        </NuxtLink>

        <div class="header__links" :class="{ scrolled: isScrolled }">
            <!-- <div class="select_lang">
                <span>RU</span>
                <img src="@/assets/img/drop_arrow.svg" alt="Выбрать язык">
            </div> -->

            <a href="#cases">Кейсы</a>
            <a href="#contacts">Оставить заявку</a>
        </div>
    </header>
    <header class="mobile" :class="{ scrolled__mob: isScrolled }">
        <NuxtLink to="/" class="header__logo">
            <img src="@/assets/img/neutron_logo.svg" alt="Логотип компании">
            <span>нейтрон</span>
        </NuxtLink>

        <div class="header__links">
            <!-- <div class="select_lang">
                <span>RU</span>
                <img src="@/assets/img/drop_arrow.svg" alt="Выбрать язык">
            </div> -->

            <a href="#cases">Кейсы</a>
        </div>

        <a href="#contacts" class="feedback" :class="{ active: !isScrolled }">Оставить заявку</a>
    </header>
</template>
<script>
export default {
    data() {
        return {
            isScrolled: false,
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            this.isScrolled = window.scrollY > 0;
        },
    },
};
</script>
<style lang="scss" scoped>
.mobile {
    display: none;
    justify-content: space-between;
    align-items: center;

    position: fixed;
    top: 15px;
    width: 100%;
    z-index: 20;

    left: 15px;
    right: 15px;

    width: calc(100% - 30px);
    transition: all .3s ease;

    padding: 6px 5px;
    padding-right: 15px;
    border-radius: 10px;

    @media (max-width: 1024px) {
        display: flex;
    }

    .feedback {
        border-radius: 64px;
        padding: 7px 25px 10px 25px;
        background: #aa7cff;

        transition: all .3s ease;

        font-weight: 500;
        font-size: 16px;
        line-height: 130%;
        color: #fff;
        font-family: var(--ibm);

        transform: scale(0);

        &:hover {
            background: #8b67cd;
        }

        &:active {
            background: #aa7cff;

        }

        position: absolute;
        right: 0;
        bottom: -60px;
    }

    .active {
        transform: scale(1);
    }

    .header__links {
        display: flex;
        align-items: center;
        gap: 30px;

        .select_lang {
            display: flex;
            align-items: center;
            gap: 5px;

            span {
                font-weight: 500;
                font-size: 16px;
                line-height: 130%;
                font-family: var(--int);
                color: #fff;
            }

        }

        a {
            font-weight: 500;
            font-size: 16px;
            line-height: 130%;
            font-family: var(--int);
            color: #fff;
            text-decoration: none;
        }
    }

    .header__logo {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;

        span {
            font-weight: 400;
            font-size: 16px;
            line-height: 130%;
            font-family: var(--hel);
            color: #fff;
        }
    }
}

.scrolled__mob {
    backdrop-filter: blur(20px);
    background: rgba(17, 17, 17, 0.7);
}

.pc {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    width: 100%;
    z-index: 20;

    padding: 50px 60px 0;

    @media (max-width: 1500px) {
        padding: 50px 40px 0;
    }

    @media (max-width: 1024px) {
        display: none;
    }

    .header__links {
        display: flex;
        align-items: center;
        gap: 50px;
        transition: all 0.3s ease;

        .select_lang {
            display: flex;
            align-items: center;
            gap: 5px;
            padding-left: 20px;
        }

        a,
        span {
            font-weight: 500;
            font-size: 20px;
            line-height: 130%;
            color: #fff;
            font-family: var(--ibm);
            cursor: pointer;
            text-decoration: none;
        }





        a {
            &:first-child {
                padding-left: 20px;
            }

            &:last-child {
                border-radius: 64px;
                padding: 12px 25px 15px 25px;
                background: #aa7cff;
                transition: all .3s ease;

                &:hover {
                    background: #8b67cd;
                }

                &:active {
                    background: #aa7cff;

                }
            }
        }
    }

    .header__logo {
        display: flex;
        align-items: center;
        gap: 20px;
        text-decoration: none;
        transition: all 0.3s ease;

        span {
            font-weight: 400;
            font-size: 36px;
            line-height: 130%;
            color: #fff;
            font-family: var(--hel);


        }
    }

    .scrolled {
        backdrop-filter: blur(20px);
        background: rgba(0, 0, 0, 0.7);
        border-radius: 20px;
        padding: 10px;
    }
}
</style>
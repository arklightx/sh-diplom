<template>
    <v-card class="mt-2">
        <v-footer padless>
            <v-card flat tile width="100%" class="lighten-1 text-center">
                <v-card-text class="text-caption d-flex text-left justify-space-between">
                    <div>
                        <div>
                            ОГРН: 1167325059582
                        </div>
                        <div>
                            ИНН: 7327078103
                        </div>
                        <div>
                            КПП: 732707810
                        </div>
                        <div>
                            Адрес: 432073,г.Ульяновск ул.Отрадная д.8а, <br>Адрес офиса: ул. Ефремова, 99
                        </div>
                    </div>
                    <div>
                        <div>
                            Руководитель: Толочко Андрей Николаевич
                        </div>
                        <div>
                            Приёмная: (8422) 27-34-70
                        </div>
                        <div>
                            Отдел по работе с населением: (8422) 27-34-70 <br>доб.240, 203
                        </div>
                        <div>
                            Аварийно диспетчерская служба: (8422) 27-44-99
                        </div>
                    </div>
                    <div>
                        <div>
                            РЕЖИМ РАБОТЫ
                        </div>
                        <div>
                            Понедельник - Пятница: с 8:00 до 17:00
                        </div>
                        <div>
                            Обед: с 12:00 до 13:00
                        </div>
                        <div>
                            Выходной: Суббота, Воскресенье
                        </div>
                        <div>
                            Прием по личным вопросам: Каждый 1 и 3<br> четверг месяца с 14-00 до 17-00
                        </div>
                    </div>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-text class="white--text">
                    {{ new Date().getFullYear() }} — <strong>ООО "Управляющая Компания"</strong>
                </v-card-text>

            </v-card>
        </v-footer>

    </v-card>
</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>
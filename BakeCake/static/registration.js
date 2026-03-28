Vue.createApp({
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            RegSchema: {
                reg: (value) => {
                    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                    if (value && emailRegex.test(value)) {
                        return true;
                    }
                    return 'Введите корректный email (например, name@domain.com)';
                }
            },
            RegInput: '',
            loading: false,
            error: ''
        }
    },
    methods: {
        async RegSubmit() {
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!this.RegInput || !emailRegex.test(this.RegInput)) {
                this.error = 'Введите корректный email (например, name@domain.com)';
                return;
            }
            
            this.loading = true;
            this.error = '';
            
            try {
                const csrftoken = this.getCookie('csrftoken');
                
                const response = await fetch('/accounts/api/auth/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({
                        email: this.RegInput
                    })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    this.RegInput = 'Регистрация успешна';
                    setTimeout(() => {
                        window.location.href = '/lk/';
                    }, 1500);
                } else {
                    this.error = data.error || 'Ошибка входа';
                    this.RegInput = '';
                }
            } catch (error) {
                console.error('Ошибка:', error);
                this.error = 'Ошибка соединения с сервером';
            } finally {
                this.loading = false;
            }
        },
        
        Reset() {
            this.RegInput = '';
            this.error = '';
            this.loading = false;
        },
        
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
}).mount('#RegModal');
new Vue({
    el: '#app',
    data:{
        a: '',
        b: '',
        c: '',
        res: '0'
    },
    methods: {
        obr(a, b, c){
            let res;
            a = +a;
            b = +b;
            c = +c;

            res = a*(4*b-3*c);
            if (isNaN(res)){
                this.res = "Error";
            } else {
                this.res = res;
            }
        },
        reset(){
            this.a = '';
            this.b = '';
            this.c = '';
            this.res =  '0';
        }

    },
    watch: {
        a(value){
            this.obr(value, this.b, this.c)
        },
        b(value){
            this.obr(this.a, value, this.c)
        },
        c(value){
            this.obr(this.a, this.b, value)
        }
    }
})
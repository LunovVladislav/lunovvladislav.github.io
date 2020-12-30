let app = new Vue({
    el: "#app",
    data: {
        mes: "5"
    },
    methods: {
        obr: function(num){
            let res = '';
            for (let i = 0; i < num.length; i++){
                res += num[i][0] + ' | ' + num[i][1] + '<br>';
            }
            return res;
        },
        sostav: function(){
            let num = Number(this.mes);
            if (typeof(num) != 'number'){
                return;
            } else {
                let res = [];
                for (let i = 1; i < num; i++){
                    res.push([i, num-i]);
                }
                return this.obr(res);
            }
        }
    }
});

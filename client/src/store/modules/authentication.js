import {login} from '@/api'
export default {
    namespaced: true,

    state: () => ({
        user: {},
        jwt: ''
    }),

    getters: {
        user: (state) => state.user,

        jwtToken: (state) => state.jwt,

        isAuthenticated(state){
            if (!state.jwt || state.jwt.split('.').length < 3) {return false}
            const data = JSON.parse(atob(state.jwt.split('.')[1]))
            const exp = new Date(data.exp * 1000) // milliseconds
            const now = new Date()
            return (now < exp)
        }
    },

    mutations:{
        setUserData(state, user){
            state.user = user
        }, 
        setJwtToken(state, jwt){
            state.jwt = jwt
        }
        
    },
    
    actions: {
        loginToDB({commit}, form){
            return login(form)
                .then(response => {
                    if (response.status === 200){
                        commit('setUserData', response.data.user)
                        commit('setJwtToken', response.data.jwt)
                    }
                    else if (response.status === 401){                                                                  
                        console.log(response.errorMessage)
                        //EventBus error
                    }
                })
                .catch(response => {
                    console.log(response.errorMessage)
                    //EventBus error
                })

        }
    }
}
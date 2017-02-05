var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function ($routeProvider) {

    $routeProvider
        .when('/', {
          templateUrl: 'static/partials/home.html',
          access: {restricted: true}
        })
        .when('/login', {
          templateUrl: 'static/partials/login.html',
          controller: 'loginController',
          access: {restricted: false}
        })
        .when('/logout', {
          controller: 'logoutController',
          access: {restricted: true}
        })
        .when('/register', {
          templateUrl: 'static/partials/register.html',
          controller: 'registerController',
          access: {restricted: false}
        })
        .when('/one', {
          template: '<h1>This is page one!</h1>',
          access: {restricted: true}
        })
        .when('/two', {
          template: '<h1>This is page two!</h1>',
          access: {restricted: false}
        })
        .otherwise({
          redirectTo: '/'
        });
});


myApp.run(function ($rootScope, $location, $route, AuthService, $http, $window) {
  // add JWT token as default auth header
  // $http.defaults.headers.common['Authorization'] = 'Bearer ' + $window.jwtToken;  

    $rootScope.$on('$routeChangeStart', function (event, next, current) {
        AuthService.getUserStatus()
            .then(function(){
                if (next.access.restricted && !AuthService.isLoggedIn()){
                  $location.path('/register');
                  $route.reload();
                }
        });
    });
});
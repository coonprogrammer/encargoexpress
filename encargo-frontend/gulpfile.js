'use strict';

const gulp = require('gulp');
const browserify = require('browserify');
const browserSync = require('browser-sync');
const buffer = require('vinyl-buffer');
const concat = require('gulp-concat');
const cssmin = require('gulp-minify-css');
const del = require('del');
const gpackage = require('./package.json');
const jshint = require('gulp-jshint');
const newer = require('gulp-newer');
const babel = require('babelify');
const run = require('gulp-run');
const sass = require('gulp-sass');
const source = require('vinyl-source-stream');
const uglify = require('gulp-uglify');
const reload = browserSync.reload;

/**
* Running Bower
*/
gulp.task('bower', () => {
    run('bower install').exec();
})

/**
* Cleaning dist/ folder
*/
.task('clean', (cb) => {
    del(['./app/*'], cb);
})

/**
* Running livereload server
*/
.task('server', () => {
    browserSync({
        server: {
            baseDir: './app' 
        }
    });
})

/**
* Sass compilation
*/
.task('sass', () => {
    return gulp.src(gpackage.paths.sass)
        .pipe(sass())
        .pipe(concat(gpackage.dest.style))
        .pipe(gulp.dest(gpackage.dest.dist));
})
.task('sass:min', () => {
    return gulp.src(gpackage.paths.sass)
        .pipe(sass())
        .pipe(concat(gpackage.dest.style))
        .pipe(cssmin())
        .pipe(gulp.dest(gpackage.dest.dist));
})

/**
* JSLint/JSHint validation
*/
.task('lint', () => {
    return gulp.src(gpackage.paths.js)
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
})

/** JavaScript compilation */
.task('js', () => {
    return browserify(gpackage.paths.app)
        .transform(
            babel.configure({
                presets: ["react"]
            })
        )
        .bundle()
        .pipe(source(gpackage.dest.app))
        .pipe(gulp.dest(gpackage.dest.dist));
})
.task('js:min', () => {
    return browserify(gpackage.paths.app)
        .transform(
            babel.configure({
                presets: ["react"]
            })
        )
        .bundle()
        .pipe(source(gpackage.dest.app))
        .pipe(buffer())
        .pipe(uglify())
        .pipe(gulp.dest(gpackage.dest.dist));
})

/**
*   Copy React and React-dom to APP
*/
.task('copy-react', () => {
    return gulp.src('./node_modules/react/dist/react.js')
        .pipe(newer(gpackage.dest.vendor + '/react.js'))
        .pipe(gulp.dest(gpackage.dest.vendor));
})
.task('copy-react-dom', () => {
    return gulp.src('./node_modules/react-dom/dist/react-dom.js')
        .pipe(newer(gpackage.dest.vendor + '/react-dom.js'))
        .pipe(gulp.dest(gpackage.dest.vendor));
})

/**
* Compiling resources and serving application
*/
.task('build', ['bower', 'clean', 'copy-react', 'copy-react-dom', 'lint', 'sass', 'js'])
.task('build:minified', ['bower', 'clean', 'copy-react', 'copy-react-dom', 'lint', 'sass:min', 'js:min'])
.task('serve', ['build', 'server'], () => {
    return gulp.watch([
        gpackage.paths.js, gpackage.paths.jsx, gpackage.paths.html, gpackage.paths.sass
    ], [
        'lint', 'sass', 'js', browserSync.reload
    ]);
})
.task('serve:minified', ['build:minified', 'server'], () => {
    return gulp.watch([
        gpackage.paths.js, gpackage.paths.jsx, gpackage.paths.html, gpackage.paths.sass
    ], [
        'lint', 'sass:min', 'js:min', browserSync.reload
    ]);
});
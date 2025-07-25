<template>
    <div class="mb-3 position-relative">
        <FloatLabel :variant="variant">
            <InputText :id="id" v-model="inputValue"
                :class="['form-control', inputClass, { 'is-invalid': invalid || (required && !inputValue && showErrorMessage) }]"
                :invalid="invalid || (required && !inputValue && showErrorMessage)" :autocomplete="autocomplete"
                v-bind="$attrs" @keypress="handleKeyPress" @input="handleInput" />
            <label :for="id" class="form-label">
                <i v-if="icon" :class="icon" class="me-2"></i>
                {{ label }}
                <span v-if="required" class="text-danger">*</span>
            </label>
        </FloatLabel>

        <div v-if="hint" class="form-text text-muted">
            {{ hint }}
        </div>

        <div v-if="(invalid || (required && !inputValue)) && showErrorMessage" class="invalid-feedback">
            Este campo es obligatorio
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';

const props = defineProps({
    id: { type: String, required: true },
    label: { type: String, required: true },
    modelValue: { type: [String, Number], default: '' },
    variant: {
        type: String,
        default: 'outlined',
        validator: (value) => ['outlined', 'filled', 'standard'].includes(value)
    },
    invalid: { type: Boolean, default: false },
    required: { type: Boolean, default: false },
    autocomplete: { type: String, default: 'off' },
    inputClass: { type: [String, Array, Object], default: '' },
    icon: { type: String, default: '' },
    hint: { type: String, default: '' },
    showErrorMessage: { type: Boolean, default: true },
    validationType: {
        type: String,
        default: '',
        validator: (value) => ['', 'dni', 'phone'].includes(value)
    }
});

const emit = defineEmits(['update:modelValue']);

const inputValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});

const handleKeyPress = (event) => {
    if (props.validationType === 'dni' || props.validationType === 'phone') {
        const keyCode = event.keyCode || event.which;
        const keyValue = String.fromCharCode(keyCode);
        const isValid = /^[0-9]*$/.test(keyValue);
        
        if (!isValid) {
            event.preventDefault();
        }
    }
};

const handleInput = (event) => {
    // Solo actualizamos el valor si no excede los límites
    if (props.validationType === 'dni' && event.target.value.length > 8) {
        inputValue.value = event.target.value.slice(0, 8);
    } else if (props.validationType === 'phone' && event.target.value.length > 9) {
        inputValue.value = event.target.value.slice(0, 9);
    }
};
</script>

<style scoped>
/* Ajustes para integrar PrimeVue con Bootstrap */

/* Estilos de validación */
.is-invalid {
    border-color: #dc3545;
    padding-right: calc(1.5em + 0.75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.375em + 0.1875rem) center;
    background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.is-invalid:focus {
    border-color: #dc3545;
    box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.invalid-feedback {
    display: block;
    width: 100%;
    margin-top: 0.25rem;
    font-size: 0.875em;
    color: #dc3545;
}
</style>
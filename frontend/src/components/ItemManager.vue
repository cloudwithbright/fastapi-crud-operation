<template>
    <div class="container">
        <h1>Item Manager</h1>
        <form @submit.prevent="createNewItem" class="form">
            <label>
                Name
                <input class="input-field" v-model="item.name" placeholder="Name" required />
            </label>
            <label>
                Description
                <input class="input-field" v-model="item.description" placeholder="Description" />
            </label>
            <label>
                Price
                <input type="float" class="input-field" v-model.number="item.price" placeholder="Price" required />
            </label>
            <label class="checkbox-label">
                <input type="checkbox" v-model="item.in_stock" /> In Stock
            </label>
            <button type="submit" class="submit-button">Create Item</button>
        </form>
<hr>
        <h2>Items</h2>
        <div class="table-container" v-if="items.length > 0">
            <table class="item-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Price</th>
                        <th>In Stock</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in items" :key="item.id">
                        <td>{{ item.name }}</td>
                        <td>{{ item.description }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.in_stock ? 'Yes' : 'No' }}</td>
                        <td>
                            <button @click="editItem(item)" class="action-button">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button @click="deleteExistingItem(item.id)" class="action-button">
                                <i class="fas fa-trash"></i>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p v-else>No items available.</p>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getItems, createItem, deleteItem } from '../api';
import { useToast } from 'vue-toastification';

export default {
    setup() {
        const items = ref([]);
        const item = ref({
            name: '',
            description: '',
            price: 0,
            in_stock: false,
        });

        const toast = useToast();

        const fetchItems = async () => {
            const response = await getItems();
            items.value = response.data;
        };

        const createNewItem = async () => {
            const response = await createItem(item.value);
            if (response.message === "Item added successfully. Thank you!") {
                items.value.push(response.data[0]);
                toast.success(response.message);
            } else if (response.message === "Item exists. Thank you!") {
                toast.info(response.message);
            }
            item.value = { name: '', description: '', price: 0, in_stock: false };
        };

        const editItem = (editableItem) => {
            item.value = { ...editableItem };
        };

        const deleteExistingItem = async (id) => {
            await deleteItem(id);
            items.value = items.value.filter(item => item.id !== id);
            toast.success('Item deleted successfully!');
        };

        onMounted(fetchItems);

        return { items, item, createNewItem, editItem, deleteExistingItem };
    },
};
</script>

<style>
#app {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    width: inherit;
}
body {
    background-color: #181818;
    color: #f0f0f0;
    font-family: Arial, sans-serif;
    height: 100%; /* Ensure body takes full height */
    margin: 0;
}

html, body {
    height: 100%; /* Ensure html and body take full height */
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; /* Center vertically */
    padding: 70px;
    background-color: #242424;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    max-width: 900px;
    height: 100%; /* Full height */
}

h1 {
    color: #ffffff;
}

h2 {
    color: #ffffff;
    margin-top: 20px;
}

.form {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    margin-bottom: 20px;
}

.input-field {
    padding: 12px;
    font-size: 16px;
    width: 100%;
    border: 1px solid #555;
    border-radius: 4px;
    margin-bottom: 15px;
    background-color: #333;
    color: #f0f0f0;
    transition: border-color 0.3s;
}

.input-field:focus {
    border-color: #007bff;
    outline: none;
}

.checkbox-label {
    margin-bottom: 15px;
    color: #f0f0f0;
}

.submit-button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.submit-button:hover {
    background-color: #0056b3;
}

.table-container {
    max-height: 300px; /* Limit height for scrolling */
    overflow-y: auto; /* Enable vertical scrolling */
    width: 100%;
}

.item-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.item-table th,
.item-table td {
    padding: 12px;
    text-align: left;
    border: 1px solid #444;
}

.item-table th {
    background-color: #007bff;
    color: white;
}

.item-table tr:nth-child(even) {
    background-color: #333;
}

.item-table tr:hover {
    background-color: #555;
}

.action-button {
    padding: 5px;
    font-size: 16px;
    cursor: pointer;
    background: none;
    border: none;
    color: #007bff;
    transition: color 0.3s;
}

.action-button:hover {
    color: #0056b3;
}
</style>